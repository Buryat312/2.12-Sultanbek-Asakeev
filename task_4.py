def func(*sum_number):
    j = 0  #zadaem peremennuiu 'j'
    for i in sum_number: #dlya  peremennoi  'i' v sum_number(eto list - b), proidis' ciklom
        try:
            j += i # j = j + i
        except: #pri vyhode kakoi libo owibki prodolzhai i ne obrashai vnimaniya na nee
            continue
    return j