#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'notebook lectures'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Tricks

#%%
pets = ["dog", "goat", "pig", "sheep", "cattle", "zebu", "cat", "chicken",
        "guinea pig", "donkey", "duck", "water buffalo",
        "western honey bee", "dromedary camel", "horse", "silkmoth",
        "pigeon", "goose", "yak", "bactrian camel", "llama", "alpaca",
        "guineafowl", "ferret", "muscovy duck", "barbary dove",
        "bali cattle", "gayal", "turkey", "goldfish", "rabbit", "koi",
        "canary", "society finch", "fancy mouse", "siamese fighting fish",
        "fancy rat and lab rat", "mink", "red fox", "hedgehog", "guppy"]

numbers = range(30)

message_dict = {"name": "Ben",
                "Year": 2017,
                "Location": "Sydney",
                "Greeting": "Yo whatup now and give a brother room",
                "Fact": "It would take 1,200,000 mosquitoes, each " +
                        "sucking once, to completely drain the " +
                        "average human of blood",
                "Alphabet Inc Class A": "847.80USD",
                "fruit": ["apple", "apricot", "avocado", "abiu"]}

#%% [markdown]
# # Slicing

#%%
# pets = range(40)
print "[:10]", pets[:10]
print "\n[35:]", pets[35:]
print "\n[4:20]", pets[4:20]
print "\n[:-35]", pets[:-35]
print "\n[::-1]", pets[::-1]
some_pets = pets[4:10]
some_pets

#%% [markdown]
# # Append vs Extend

#%%
new_list = []
new_list.append(numbers)
new_list.append(some_pets)
print new_list


#%%
another_new_list = []
another_new_list.extend(numbers)
another_new_list.extend(some_pets)
print another_new_list

#%% [markdown]
# # Truthy values

#%%
thing = False
if thing:
    print "You'll never see me"


#%%
thing = "hi!"
if thing:
    print "Woah, look at me!" 


#%%
thing = None
if thing:
    print "I'm a sneaky snake"

#%% [markdown]
# # List comprehensions

#%%
pet_name_lengths = []
for p in pets:
    pet_name_lengths.append(len(p))
    
print pet_name_lengths


#%%
pet_name_lengths = [len(p) for p in pets]
print pet_name_lengths

#%% [markdown]
# # λambdas 

#%%
def get_2x_len(my_string):
    return len(my_string) * 2

print map(get_2x_len, pets)


#%%
# print map(lambda x: len(x) * 2, pets)
print map(lambda x: x[1], pets)


#%%
print map(len, pets)

#%% [markdown]
# # Built ins

#%%
from random import randint
my_odd_list = [randint(0,100) for _ in range(1000)]


#%%
max(my_odd_list)


#%%
min(my_odd_list)


#%%
zip(range(len(pets)), pets)


#%%
for p in enumerate(pets):
    print p

#%% [markdown]
# # Generators

#%%
a = enumerate(pets)
a.next()


#%%
def a_generator():
    counter = 0
    while True:
        yield counter
        counter += 3
        
g = a_generator()

print g.next()
print g.next()
print g.next()

#%% [markdown]
# # Dictionary comprehensions

#%%
# all yours terry!
L = range(10)
d = {k:v for k, v in zip(pets, L)}
print d
import collections
d = collections.defaultdict(list)
d = collections.Counter()
d = collections.Counter(my_odd_list)
print d
print max(d, key=lambda x: d[x])


