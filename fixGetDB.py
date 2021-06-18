def get_DB(browser,DB=[],dfg=pd.DataFrame(),sleep=0.8,DIR='InstituLAC',
           start=None,end=None,COL_Group='',start_time=0):
    os.makedirs(DIR,exist_ok=True)
    if dfg.empty:
        browser,dfg=get_groups(browser,DIR=DIR,sleep=sleep)
    dfg = dfg.reset_index(drop=True)

    #find start and end if COL_Group
    if COL_Group:
        dfcg=dfg[dfg['COL Grupo']==COL_Group]
        if not dfcg.empty:
            start=dfcg.index[0]
            end=start+1
    #assert dfg.shape[0] == 324
    # DICT CAT-PRODS-TAB
    dict_tables_path = str(pathlib.Path(__file__).parent.absolute()) + '/dict_tables.json'
    with open(dict_tables_path) as file_json:
       dict_tables=json.loads(file_json.read())    
    #with open('dict_tables.json') as file_json:
    #    dict_tables=json.loads(file_json.read())

    time.sleep(sleep*2)

    LP = []
    LR = [] 
    for idx in dfg.index[start:end]:       # TEST

        # create db for store things related to group
        DBG = {}

        # part info group
        print(dfg.loc[idx,'Nombre del grupo'])

        # specific group url
        time.sleep(sleep)
        url_group = dfg.loc[idx,'Revisar']

        # go to url group
        time.sleep(sleep)
        browser.get(url_group)

        # catch two tables: info grupo and  members
        source=browser.page_source

        #info
        l_info=pd.read_html(source, match='Nombre Grupo')
        info_g=l_info[3].pivot(columns=0,values=1)

        # STORE INFO_GROUP
        DBG['Info_group'] = info_g

        # members
        l_int = pd.read_html(source,attrs={'id':'tblIntegrantes'},header=2)
        mem_g=l_int[0]

        # STORE_MEMBERS
        DBG['Members'] =  mem_g

        # Products

        #time.sleep(sleep*5) # time time time !!!
        h.wait_until(lambda: browser.find_element_by_xpath('//td[@id="bodyPrincipal"]//a[text()="Ver productos"]') is not None)
        h.click(browser.find_element_by_xpath('//td[@id="bodyPrincipal"]//a[text()="Ver productos"]'))

        # products by belongs to  # time time time
        #time.sleep(sleep*7)       # time time time
        h.wait_until(lambda: browser.find_element_by_xpath('//*[@id="ProdsPertenecia"]') is not None)
        h.click(browser.find_element_by_xpath('//*[@id="ProdsPertenecia"]'))

        time.sleep(sleep)
        url_products=browser.current_url


        # map all products, store those id categories that amount is different to 0 and id products asociated.
        # make queries with combinations of categories and products
        # make urls with diferent combinations of quieries
        # go to each of urls
        # load page source
        # catch table ( or tables) asociated with categories and products
        # store tables

        report = ''

        list_of_prods =[] #[[cat,prod],[cat,prod]...]

        # map all products and get products and subs diff to cero
        for i in browser.find_elements_by_xpath('//div[@id="accordionCatgP"]/h3'):

            report += i.text + '\n' 
            report += i.get_attribute('id') + '\n'     

            time.sleep(sleep)
            h.click(i)

            # cat
            cat_ = int(re.findall(r'\d+',i.text)[0])

            # create cat key in dict, for estore diferents products by this categori: 'NC_': {'ART_E':TABLE,
            #                                                                                 'ART_IMP':TABLE}
            if cat_ > 0:
                DBG[i.get_attribute('id')] = {}


            for j in browser.find_elements_by_xpath('//div[@aria-labelledby="%s"]/h3' % i.get_attribute('id')):

                report += '\t' + j.text + '\n' 
                report += '\t' + j.get_attribute('id') + '\n'

                #prod
                pro_ = int(re.findall(r'\d+', j.text)[0])

                if cat_ > 0 and pro_ > 0:  

                    list_of_prods.append([i.get_attribute('id'),j.get_attribute('id')])

            time.sleep(sleep) 
            # h.click(a)
            h.click(i)

        # PAR: products with revisions
        time.sleep(sleep*3) #DEBUG TIME
        h.wait_until(lambda: browser.find_element_by_xpath('//*[@id="ProdsAval"]'))
        h.click(browser.find_element_by_xpath('//*[@id="ProdsAval"]'))

        # NC

        _NC = browser.find_element_by_xpath('//*[@id="NC"]')

        h.click(_NC)

        cat_ = int(re.findall(r'\d+',_NC.text)[0])

        LIB = browser.find_element_by_xpath('//*[@id="LIB"]')

        L = int(re.findall(r'\d+', LIB.text)[0])

        CAP_LIB = browser.find_element_by_xpath('//*[@id="CAP_LIB"]')

        CL = int(re.findall(r'\d+', CAP_LIB.text)[0])

        if (cat_ > 0 and L > 0) or (cat_ > 0 and CL > 0):

            DBG[_NC.get_attribute('id')] = {}

        if (cat_ > 0 and L > 0):

            list_of_prods.append([_NC.get_attribute('id'),LIB.get_attribute('id')])

        if (cat_ > 0 and CL > 0):

            list_of_prods.append([_NC.get_attribute('id'),CAP_LIB.get_attribute('id')])

        # print(report)
        # print('\n')
        # print('--------------------------------')
        time.sleep(sleep*2)

        tables=[]

        for p in range(len(list_of_prods)):

                # make query
                if list_of_prods[p][0] == 'NC':

                    query='categoria=%s&subcategoria=%s&aval=T' % (list_of_prods[p][0],list_of_prods[p][1])

                else:

                    query='categoriaP=%s&subcategoriaP=%s&aval=P' % (list_of_prods[p][0],list_of_prods[p][1])

                # make url query
                url_query = url_products.split('?')[0] + '?' + query + '&' + url_products.split('?')[1]

                # retrieve id asociated tables
                table_id = dict_tables[list_of_prods[p][0]][list_of_prods[p][1]]

                # go to url product by group
                time.sleep(sleep)

                try_var = 0
                bool_var = True
                ### fix missing tables internet connection problem
                while bool_var:

                    if try_var == 3:
                        bool_var = False
                    
                    browser.get(url_query)

                    # load page
                    time.sleep(sleep)
                    page_source = browser.page_source

                    # catch tables
                    if isinstance(table_id,str): # case one table

                        # catch title table

                        #title_table = browser.find_element_by_xpath('//div/p[@class="titulo_tabla"]').text 
                        # cathc table
                        print(url_query)
                        time.sleep(sleep*2)
                        
                        try:
                            table = pd.read_html(page_source,attrs={'id':table_id}, header=2)[0][1:-1]

                            if table.shape[1] > 0:
                                bool_var = False

                        except ValueError:
                            table=None

                        # store table
                        DBG[list_of_prods[p][0]][list_of_prods[p][1]] = {table_id:table}
                        # ---- in building ----

                    elif isinstance(table_id, list): # case multiple tables

                        DBG[list_of_prods[p][0]][list_of_prods[p][1]] ={}

                        for i in range(len(table_id)):

                            # fix bug
                            if list_of_prods[p][1] == 'DC_P' and i == 3:
                                # catch title specific table 
                                title_table = browser.find_elements_by_xpath('//div/p[@class="titulo_tabla"]')[i].text

                                # catch table software
                                table = pd.read_html(page_source,attrs={'id':table_id[i]}, header=2)[1][1:-1]

                                # store table
                                DBG[list_of_prods[p][0]][list_of_prods[p][1]]['DC_DES_P_TABLE'] = table

                            # catch title specific table 
                            title_table = browser.find_elements_by_xpath('//div/p[@class="titulo_tabla"]')[i].text

                            # catch table trasmedia
                            table = pd.read_html(page_source,attrs={'id':table_id[i]}, header=2)[0][1:-1]

                            # store table
                            DBG[list_of_prods[p][0]][list_of_prods[p][1]][table_id[i]]=table

                    try_var += 1


                        # -----------
        DB.append(DBG)
        LP.append(list_of_prods)
        LR.append(report)

        with open(f'{DIR}/DB.pickle', 'wb') as f:
            pickle.dump(DB, f)

        print(time.time()-start_time)

    browser.close()    
    return DB,dfg