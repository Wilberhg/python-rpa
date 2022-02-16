from buscador import Google

obj = Google('http://www.google.com')
obj.acessa_site()
obj.efetua_busca('Python')
obj.clica_botao()

obj2 = Google('http://www.bing.com')
obj2.acessa_site()
obj2.efetua_busca('JavaScript')
obj2.clica_botao()

...