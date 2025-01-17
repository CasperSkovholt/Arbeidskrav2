#!/usr/bin/env python
# coding: utf-8

# ## Oppgave 1

# In[6]:


alder = int(input("Hvilket år er du født"))

nåværende_år = 2025

alder_i_2025 = nåværende_år - alder

print(f"I løpet av året {nåværende_år} blir jeg {alder_i_2025} år gammel.")


# ## Oppgave 2

# In[14]:


import math 
# for å ikke få eks 6.0 pizzaer må man bruke int og ikke float. 
antall_elever = int(input("Skriv inn antall elever:"))

antall_pizzaer = math.ceil(antall_elever / 4)

print(f"Til klassefesten med {antall_elever} må det kjøpes {antall_pizzaer} pizzaer.")


# ## Oppgave 3

# In[15]:


import numpy as np

def grader_til_radianer(v_grad):
    return v_grad * np.pi / 180

v_grad = float(input('Skriv inn gradtallet: '))

v_rad = grader_til_radianer(v_grad)

print(f'Vinkelen {v_grad} grader tilsvarer {v_rad:.4f} radianer.')


# ## Oppgve 4

# #### A)

# In[16]:


data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
}


# #### B)

# In[18]:


land = input("Skriv inn et land: ")

if land in data:
    hovedstad, innbyggere = data[land]
    print(f"{hovedstad} er hovedstaden i {land} og det er {innbyggere} mill. innbyggere i {hovedstad}.")


# In[19]:


nytt_land = input("Skriv inn et nytt land: ")

if nytt_land in data:
    print(f"{nytt_land} finnes allerede i databasen.")
else:
    hovedstad = input(f"Skriv inn hovedstaden i {nytt_land}: ")
    innbyggere = float(input(f"Skriv inn antall innbyggere (i mill.) i {hovedstad}: "))
    
    data[nytt_land] = [hovedstad, innbyggere]
    print(f"{nytt_land} har blitt lagt til i databasen.")

print("Oppdatert database:")
for land, info in data.items():
    print(f"{land}: Hovedstad = {info[0]}, Innbyggere = {info[1]} mill.")


# ## Oppgave 5

# In[20]:


def beregn_areal_og_omkrets(a, b):
    c = math.sqrt(a**2 + b**2)
    
    radius = b / 2
    
    trekant_areal = (a * b) / 2
    halvsirkel_areal = (math.pi * radius**2) / 2
    total_areal = trekant_areal + halvsirkel_areal
    
    halvsirkel_omkrets = math.pi * radius
    ytre_omkrets = a + b + c + halvsirkel_omkrets
    
    return total_areal, ytre_omkrets

a = float(input("Skriv inn lengden på a (kateten til trekanten): "))
b = float(input("Skriv inn lengden på b (kateten til trekanten): "))

areal, omkrets = beregn_areal_og_omkrets(a, b)

print(f"Arealet av figuren er {areal:.2f} kvadratmeter.")
print(f"Den ytre omkretsen av figuren er {omkrets:.2f} meter.")


# ## Oppgave 6

# In[30]:


import matplotlib.pyplot as plt

def f(x):
    return -x**2 - 5

x = np.linspace(-10, 10, 200)
y = f(x)

plt.plot(x, y, label="f(x) = -x² - 5")

plt.title("Grafen til f(x) = -x² - 5")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()


# In[ ]:




