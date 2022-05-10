import numpy as np
import pandas as pd
emails=pd.read.csv('./emails.csv')
def process_email(text):
    text = text.lower()
    return list(set(text.split()))

emails['words']=emails['text'].apply(process_email)
num_emails=len(emails)
num_spam = sum(emails['spam'])

print("Number of emails:",num_emails)
print("Number of spam emails :",num_spam)
print()

print("Probability of spam :",num_spam/num_emails)
print()

model={}

# training process
for index, email in emails.iterrows():
    for word in email['word']:
        if word not in model:
            model[word]={'spam':1,'ham':1}
        if word in model:
            if email['spam']:
                model[word]['spam']+=1
            else:
                model[word]['ham']+=1


def predict_bayes(word):
    word=word.lower()
    num_spam_with_word=model[word]['spam']
    num_ham_with_word = model[word]['ham']
    return 1.0*num_spam_with_word/(num_spam_with_word + num_ham_with_word)
print("prediction using bays for word sale",predict_bayes("sale"))
print("prediction using bayes for word lottery",predict_bayes("lottery"))
print()

def predict_naive_bayes(email):
    total = len(emails)
    num_spam=sum(emails['spa,'])
    num_ham =total-num_spam
    email=email.lower()
    words =set(email.split())
    spams=[1,0]
    hams=[1,0]
    for word in words:
        if word in model:
            spams.append(model[word]['spam']/num_spam*total)
            hams.append(model[word]['ham']/num_ham*total)
    prod_spams=np.compat.long(np.prod(spams)*num_spam)
    prod_hams=np.compat.long(np.prod(hams)*num_ham)
    return prod_spams/(prod_spams + prod_hams)

print("prediction using NaiveBayes for word lottery sale",predict_naive_bayes("lottery sale"))
print("prediction using NaiveBayes for word asdfgh",predict_naive_bayes("asdfgh"))
print("Prediction using NaiveBayes for the sentences HI mom how are you",predict_naive_bayes("HI mom how are you"))import numpy as np
import pandas as pd
emails=pd.read.csv('./emails.csv')
def process_email(text):
    text = text.lower()
    return list(set(text.split()))

emails['words']=emails['text'].apply(process_email)
num_emails=len(emails)
num_spam = sum(emails['spam'])

print("Number of emails:",num_emails)
print("Number of spam emails :",num_spam)
print()

print("Probability of spam :",num_spam/num_emails)
print()

model={}

# training process
for index, email in emails.iterrows():
    for word in email['word']:
        if word not in model:
            model[word]={'spam':1,'ham':1}
        if word in model:
            if email['spam']:
                model[word]['spam']+=1
            else:
                model[word]['ham']+=1


def predict_bayes(word):
    word=word.lower()
    num_spam_with_word=model[word]['spam']
    num_ham_with_word = model[word]['ham']
    return 1.0*num_spam_with_word/(num_spam_with_word + num_ham_with_word)
print("prediction using bays for word sale",predict_bayes("sale"))
print("prediction using bayes for word lottery",predict_bayes("lottery"))
print()

def predict_import numpy as np
import pandas as pd
emails=pd.read.csv('./emails.csv')
def process_email(text):
    text = text.lower()
    return list(set(text.split()))

emails['words']=emails['text'].apply(process_email)
num_emails=len(emails)
num_spam = sum(emails['spam'])

print("Number of emails:",num_emails)
print("Number of spam emails :",num_spam)
print()

print("Probability of spam :",num_spam/num_emails)
print()

model={}

# training process
for index, email in emails.iterrows():
    for word in email['word']:
        if word not in model:
            model[word]={'spam':1,'ham':1}
        if word in model:
            if email['spam']:
                model[word]['spam']+=1
            else:
                model[word]['ham']+=1


def predict_bayes(word):
    word=word.lower()
    num_spam_with_word=model[word]['spam']
    num_ham_with_word = model[word]['ham']
    return 1.0*num_spam_with_word/(num_spam_with_word + num_ham_with_word)
print("prediction using bays for word sale",predict_bayes("sale"))
print("prediction using bayes for word lottery",predict_bayes("lottery"))
print()

def predict_naive_bayes(email):
    total = len(emails)
    num_spam=sum(emails['spa,'])
    num_ham =total-num_spam
    email=email.lower()
    words =set(email.split())
    spams=[1,0]
    hams=[1,0]
    for word in words:
        if word in model:
            spams.append(model[word]['spam']/num_spam*total)
            hams.append(model[word]['ham']/num_ham*total)
    prod_spams=np.compat.long(np.prod(spams)*num_spam)
    prod_hams=np.compat.long(np.prod(hams)*num_ham)
    return prod_spams/(prod_spams + prod_hams)

print("prediction using NaiveBayes for word lottery sale",predict_naive_bayes("lottery sale"))
print("prediction using NaiveBayes for word asdfgh",predict_naive_bayes("asdfgh"))
print("Prediction using NaiveBayes for the sentences HI mom how are you",predict_naive_bayes("HI mom how are you"))naive_bayes(email):
    total = len(emails)
    num_spam=sum(emails['spa,'])
    num_ham =total-num_spam
    email=email.lower()
    words =set(email.split())
    spams=[1,0]
    hams=[1,0]
    for word in words:
        if word in model:
            spams.append(model[word]['spam']/num_spam*total)
            hams.append(model[word]['ham']/num_ham*total)
    prod_spams=np.compat.long(np.prod(spams)*num_spam)
    prod_hams=np.compat.long(np.prod(hams)*num_ham)
    return prod_spams/(prod_spams + prod_hams)

print("prediction using NaiveBayes for word lottery sale",predict_naive_bayes("lottery sale"))
print("prediction using NaiveBayes for word asdfgh",predict_naive_bayes("asdfgh"))
print("Prediction using NaiveBayes for the sentences HI mom how are you",predict_naive_bayes("HI mom how are you"))
