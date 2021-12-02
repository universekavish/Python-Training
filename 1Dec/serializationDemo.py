import pickle

#serialization process
L = [10, 20, 'Hello', [30, 40], {1:2, 3:4}, 50]
fout = open('mydata.serialized', 'wb')
pickle.dump(L, fout)
fout.close()


#Deserialization
fin = open('mydata.serialized', 'rb')
L1 = pickle.load(fin)
fin.close()
print(L1)