#!/usr/bin/env python
# coding: utf-8

# In[27]:


import networkx as nx
g=nx.Graph()
nodes_to_add = ['b', 'c', 'd','e','a']
g.add_nodes_from(nodes_to_add)
edges_to_add = [('a', 'c'), ('b', 'c'), ('c', 'd'),('a','e'),('a','b')]
g.add_edges_from(edges_to_add)
nx.draw(g, with_labels=True)
nx.is_tree(g)


# In[28]:




nx.draw(g,
        with_labels=True,
        node_color='blue',
        node_size=1600,
        font_color='white',
        font_size=16,
        )


# In[29]:


g.nodes()


# In[30]:


g.edges()


# In[31]:


for node in g.nodes:
    print(node)


# In[32]:


for edge in g.edges:
    print(edge)


# In[37]:


g.number_of_nodes()


# In[38]:


g.number_of_edges()


# In[39]:


for neighbor in g.neighbors('b'):
    print(neighbor)


# In[40]:


list(G.neighbors('b'))


# In[42]:


nx.is_tree(g)


# In[43]:


nx.is_connected(g)


# In[44]:


g.has_node('a')


# In[45]:


g.has_node('z')


# In[46]:


'a' in g.nodes


# In[48]:


g.has_edge('a', 'b')


# In[49]:


g.has_edge('c', 'e')


# In[50]:


('c', 'd') in g.edges


# In[51]:


len(list(g.neighbors('a')))


# In[55]:


g.degree('c')


# In[ ]:





# In[ ]:




