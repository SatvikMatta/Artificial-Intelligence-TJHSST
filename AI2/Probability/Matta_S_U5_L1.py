from pomegranate import *

#Part A

Graduate = DiscreteDistribution({'graduate':0.9, 'no-graduate':0.1})

Offer1 = ConditionalProbabilityTable([
['graduate', 'offer', 0.5],
['graduate', 'no-offer', 0.5],
['no-graduate', 'offer', 0.05],
['no-graduate', 'no-offer', 0.95]], [Graduate])

Offer2 = ConditionalProbabilityTable([
['graduate', 'offer', 0.75],
['graduate', 'no-offer', 0.25],
['no-graduate', 'offer', 0.25],
['no-graduate', 'no-offer', 0.75]], [Graduate])

s_graudate = State(Graduate, 'graduation')
s_offer_1 = State(Offer1, 'offer_1')
s_offer_2 = State(Offer2, 'offer_2')
model = BayesianNetwork('graduation')
model.add_states(s_graudate, s_offer_1,s_offer_2)
model.add_transition(s_graudate, s_offer_1)
model.add_transition(s_graudate, s_offer_2)
model.bake() # finalize the topology of the model
print ('The number of nodes:', model.node_count())
print ('The number of edges:', model.edge_count())
# predict_proba(Given factors)
# P(Offer1|Graduate)
print (model.predict_proba({'graduation':'graduate'})[1].parameters)
# P(Graduate|Offer1, Offer2)
print (model.predict_proba({'offer_1':'offer','offer_2':'offer'})[0].parameters)
# P(Graduate|~Offer1, Offer2)
print (model.predict_proba({'offer_1':'no-offer','offer_2':'offer'})[0].parameters)
# P(Graduate|~Offer1, ~Offer2)
print (model.predict_proba({'offer_1':'no-offer','offer_2':'no-offer'})[0].parameters)
# P(Offer2 | Offer1)
print(model.predict_proba({'offer_1':'offer'})[2].parameters)

#Part B
print()
Sunny = DiscreteDistribution({'sunny': 0.7, 'no-sunny': 0.3})
Rainy = DiscreteDistribution({'rainy': 0.01, 'no-rainy': 0.99})
Happy = ConditionalProbabilityTable([
['sunny', 'rainy', 'happy', 1],
['sunny', 'rainy', 'no-happy', 0],
['no-sunny', 'rainy', 'happy', 0.9],
['no-sunny', 'rainy', 'no-happy', 0.1],
['sunny', 'no-rainy', 'happy', 0.7],
['sunny', 'no-rainy', 'no-happy', 0.3],
['no-sunny', 'no-rainy', 'happy', 0.1],
['no-sunny', 'no-rainy', 'no-happy', 0.9]], [Sunny, Rainy])
s_sunny = State(Sunny, 'Sunny')
s_rainy = State(Rainy, 'Rainy')
s_happy = State(Happy, 'Happy')
model = BayesianNetwork('sunny')

model.add_states(s_sunny, s_rainy, s_happy)
model.add_transition(s_sunny, s_happy)
model.add_transition(s_rainy, s_happy)
model.bake() # finalize the topology of the model
print ('The number of nodes:', model.node_count())
print ('The number of edges:', model.edge_count())

#P(rainy | sunny)
print(model.predict_proba({'Sunny':'sunny'})[1].parameters)
#P(rainy | happy, sunny)
print(model.predict_proba({'Sunny':'sunny', 'Happy':'happy'})[1].parameters)
#P(rainy | happy)
print(model.predict_proba({'Happy':'happy'})[1].parameters)
#P(rainy | happy, ~sunny)
print(model.predict_proba({'Happy':'happy', 'Sunny':'no-sunny'})[1].parameters)
