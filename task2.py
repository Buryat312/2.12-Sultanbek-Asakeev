#10 points
first = 'Advertising companies say advertising is necessary and important. It informs people about new products. Advertising hoardings in the street make our environment colorful. And adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next program in the mini-drama. Advertising can educate, too. Adverts tell us about new, healthy products. And adverts in magazines give us ideas for how to look prettier, be fashionable and be successful. Without advertising, life is boring and colorless.But some consumers argue that advertising is a bad thing. They say that advertising is bad for children. Adverts make children ‘pester’ their parents buy things for them. Advertisers know we love our children and want to give them everything. So they use children’s ‘pester power’ to sell their products. Finally, consumers say, if there is advertising there must be rules. Some adverts advertise unhealthy things like cigarettes and make people waste their money.'
second = first.lower()
# print(second)

t_count = 0
s_count = 0
for i in second:
    if i == 't':
        t_count+=1
    elif i == 's':
        s_count+=1
print(f' t - {t_count} and s - {s_count}')

advert_change = second.replace('advert', 'ADVERT')
print(advert_change)





# advert1 = 0
# word_advert = first.split()
# text = ""
# for word_a in word_advert:
#     if "ADVERT" in word_a.upper():
#         advert1+=1
#         text=(" "+word_a.upper())
#     else:
#         text=(" "+word_a)
#         first = text
# print(first)
# print(f'Words with "advert": {advert1}')


        
