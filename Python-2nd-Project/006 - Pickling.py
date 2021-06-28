import pickle

imelda = ('More Mayhem',
          'Imelda May',
          '2011',
          (1, 'Pulling the Rug'),
          (2, 'Psycho'),
          (3, 'Mayhem'),
          (4, 'Kentish Town Waltz'))

with open('Imelda.pickle', 'wb') as pickle_file:
    pickle.dump(imelda, pickle_file)

# =====================================================================

with open('Imelda.pickle', 'rb') as imelda_pickled:
    imelda2 = pickle.load(imelda_pickled)

# print(imelda2)
for item in imelda2:
    print(item)
