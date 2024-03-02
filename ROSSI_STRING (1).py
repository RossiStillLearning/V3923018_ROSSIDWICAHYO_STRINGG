#!/usr/bin/env python
# coding: utf-8

# In[1]:


nama_lengkap = input ("Masukkan Nama Anda : " )

#Menghitung jumlah huruf dari nama lengkap
jumlah_huruf = len (nama_lengkap.replace(" ", ""))

#Menghituung jumlah huruf vokal dari nama lengkap
huruf_vokal = "aiueoAIUEO"
jumlah_vokal = len([char for char in nama_lengkap if char in huruf_vokal])

#Menghitung jumlah huruf konsonan dari nama lengkap
jumlah_konsonan = jumlah_huruf - jumlah_vokal

print ("jumlah huruf dari nama lengkap anda adalah : ", jumlah_huruf)
print ("jumlah huruf vokal dari nama lengkap anda adalah : ", jumlah_vokal)
print ("jumlah huruf konsonan dari nama lengkap anda adalah : ", jumlah_konsonan)


# In[ ]:





# In[ ]:




