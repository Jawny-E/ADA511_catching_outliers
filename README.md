# Catching cheaters using an methods from ADA511
The problem of cheating has long plauged higher-education. Under immense pressure to meet high expectations some will, sacrifice their integrity for the hope of a higher grade. Institutions have to fight an uphill-battle to try to keep pace with the arms-race of ever-evoloving cheating methods. The emphasis cannot only be on prevention, but also on swift decisive action against those who chose dishonesty.

*Scenario: You are a university lecturer and you have been informed by the examination montiors that they caught a glimpse of one student in your class  using their phone during the end-of-year exam. The monitor could not identify the The university is pressuring you to identify the wronging party. You have all the exam answers, but is that enough? Can you employ techiques from ADA511 to assign probabilities of being the cheater to the different students?*

This project is inspired by a Code-Jam Qualification round in 2021, which gives the following additional information about the scenario:
![alt text](resources/codejam.png)

This material is not available online anymore, we had to employ the waybackmachine to get the problem description. We have further made adjustments to make the amount of students, the amount of questions and the probability of cheating on any given question variables so that it's simple to retest for your presumed scenario. 

The scenario itself gives us the following information of probability:
$P(success|non-cheater, Z)=f(S_i-Q_i)$
$P(success|cheater, Z)=0.5\cdot 1 + 0.5f(S_i-Q_i)$
$P(cheater)= \frac{1}{students} = 1-P(non-cheater)$
$P(Q_i=q|Z)=\frac{1}{(6\cdot 10^{accuracy})+1}$ e.g. if you use 0 decimal places, it would be $P(Q_i=q|Z)=\frac{1}{6+1}$
$P(S_i=s|Z)=\frac{1}{(6\cdot 10^{accuracy})+1}$ e.g. if you use 2 decimal places, it would be $P(Q_i=q|Z)=\frac{1}{600+1}$

## Some cool Background info
Some related subjects we looked into during the subject, that are interesting reading for the problem at hand
### The Sigmoid Function
The Sigmoid function is a logistic function written as follows: $ \sigma(x) = \frac{1}{1+e^{-x}} $. It forms an monotonically increasing S-shaped curve with range [0,1] and domain [-$\infty$,$\infty$]. It is often used as an activation function in neural networks. The function is also used frequently to model probabilities of binary outcomes in logistic regression. We then in our case assume the modelling has already been completed (by the lovely people hosting Code Jam, or maybe yourself), and we have found the relationship between the probabilty of getting something correct and the values for player Skill[-3,3] and question Difficulty[-3,3]
![alt text](resources/sigmoid.png)

Possible limitiations in our project: over-simplifying of the real-world events and assumption of independece of questions from one another. 
### Binomial and Normal distribution

### Z-scores

## Project description
In short the goal of this project is to identetify outliers, who are not "natural" outliers in the population. This work will mostly be done through assumptions of behaviour, and 

and attempt to determine if they're truly a natural outlier, or if they've used other means to acheive their results. 
![](resources/saitamaOutlier.png)

### Datasets
The project includes a Python script that can create datasets for you. The number of students and questions are set as global variables, as well as the probabiltiy for the cheater successfully checking their phone.
Here are some small examples of our datasets:

#### Exam-results by player
|Index|Truthfulness|Skill|S0 |S1 |S2 |S3 |S4 |S5 |S6 |S7 |S8 |S9 |
|-----|------|-----|---|---|---|---|---|---|---|---|---|---|
|0    |t     |-1.6 |1  |1  |0  |0  |0  |0  |0  |0  |0  |0  |
|1    |t     |-0.1 |0  |1  |0  |0  |0  |1  |1  |1  |1  |1  |
|2    |t     |1.9  |1  |1  |1  |0  |1  |1  |1  |1  |0  |1  |
|3    |c     |0.7  |1  |1  |1  |1  |1  |1  |1  |1  |1  |1  |
|4    |t     |0.5  |1  |1  |1  |0  |0  |1  |1  |1  |1  |1  |
|5    |t     |0.4  |1  |1  |0  |1  |0  |1  |1  |1  |1  |1  |
|6    |t     |0.5  |1  |1  |1  |0  |0  |1  |1  |1  |1  |1  |
|7    |t     |0.4  |1  |0  |0  |0  |1  |1  |1  |1  |1  |1  |
|8    |t     |-0.2 |1  |1  |0  |1  |0  |1  |1  |0  |0  |1  |
|9    |t     |0.1  |0  |1  |0  |0  |0  |1  |1  |1  |1  |1  |

#### Results by question
|Index|Diffuculty|S0  |S1 |S2 |S3 |S4 |S5 |S6 |S7 |S8 |S9 |
|-----|----------|----|---|---|---|---|---|---|---|---|---|
|0    |0.9       |1   |0  |1  |1  |1  |1  |1  |1  |1  |0  |
|1    |-1.9      |1   |1  |1  |1  |1  |1  |1  |0  |1  |1  |
|2    |0.3       |0   |0  |1  |1  |1  |0  |1  |0  |0  |0  |
|3    |1.5       |0   |0  |0  |1  |0  |1  |0  |0  |1  |0  |
|4    |1.1       |0   |0  |1  |1  |0  |0  |0  |1  |0  |0  |
|5    |-1.7      |0   |1  |1  |1  |1  |1  |1  |1  |1  |1  |
|6    |-0.8      |0   |1  |1  |1  |1  |1  |1  |1  |1  |1  |
|7    |-2.0      |0   |1  |1  |1  |1  |1  |1  |1  |0  |1  |
|8    |-1.4      |0   |1  |0  |1  |1  |1  |1  |1  |0  |1  |
|9    |-1.7      |0   |1  |1  |1  |1  |1  |1  |1  |1  |1  |

Here we can see that we have the following variates in the datasets are as follows:
| **Variate**         	| **Shorthand** 	| **Quantity** 	| **Domain** 	| **Description**                                        	|
|---------------------	|---------------	|--------------	|------------	|--------------------------------------------------------	|
| Intelligence(Skill) 	| I             	| Interval     	| [-3, 3]    	| Binomially spaced interval                             	|
| Difficulty          	| D             	| Interval     	| [-3, 3]    	| Uniform interval                                       	|
| Success_n           	| S_n           	| Binary       	| [0, 1]     	| Binary value, 0 denotes a failure, 1 denotes a success 	|
| Truthfulness        	| T             	| Binary       	| [t, c]     	| Binray value, 't' indicates truthful, 'c' indicates    	|

### Solutions

#### Method 0: Just test scores
If you do not know the Intelligence of the student, Truthfulness or the Difficulty of the question. All you have to base your assumption on is the set of Successes. It is here virtually impossible to differentiate between a true outlier or a cheater. You could use the following definitions to try to determine the cheater, but you would quickly find that you will end up accusing the best-scorer every single exam. 
- $P(S_1=success | S_2=success, Z) = P(S_1= success| Z)$
- $P(T=cheater) = 1 - (totalscore=score ∨ totalscore=score+1 ∨ totalscore=score+2 ∨ ... |Z)$

#### Method 1: Test scores and skill-levels
The second possible way of looking at this problem is to assume that every answer is independent of each other, and that the student has equal probabilty of answering correctly on every single question, given a previously established intelligence(skill) score. We can then learn about a quantity from similar quantities. To find the probaility of Success appearing equally or more times than the student achived. We then identify the dishonest outlier as the person with the lowest probability of scoring as they did or lower
We can then use the following relations:
- $P(S_1=success | S_2=success, Z) = P(S_1= success, Z)$
- $P(T=cheater|I=i, Z) = 1 - P(totalscore=score ∨ totalscore=score+1 ∨ totalscore=score+2 ∨ ...| I=i, Z)$
- $P(totalscore=s|I=i, Z) = \binom{n}{k}\cdot p^{k}\cdot (1-p)^{n-k}$, where $n$ is the number of questions, $k$ is the number of successes and $p$ is the probability of a success. $p$ assumed to be the result of the sigmoid function dependent only on intelligence
 
#### Method 2: Knowing scores, skills and difficulties, identify how




#### Method 3: Scenario expansion, you are only responsible for parts of the exam
In many university courses it is common for several lecturers to share the responsibility of teaching and grading a singe course. An example of this is ADA512, which is a combination of IoT, Networking and Control Systems. Limiting you in your dataset of the students.

#### Method 4: A simple application of neural networks

## How to install and setup the project
This project has inbuilt GitHub actions, where all methods in the final directory are ran and tested. It is set up to run both when an update is made to a Pull Request and manually from dispatch, you can edit this to fit your workflow better. Fork this repository to quickly take advantage of these methods. 
![alt text](resources/actions.png)
Otherwise the files should be simple enough to download and run by yourself, all Python libraries used are listed in the file requirements.txt.
### Results
None of the methods in the project can boast perfect identification of the cheater, and some methods assume information that might be impossible to estimate in a real-life situation. The methods applied here might better be called an exploration of the scenario using ADA511, than a defintive solution. However, it must be mentioned that XYZ
