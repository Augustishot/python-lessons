m_score = float(input('What is your math score?'))
e_score = float(input('What is your Englesh score?'))
if m_score >= 90 and e_score >= 90:
    print('Congratulations! You will get a price!')
elif m_score == 100 or e_score == 100:
    print("Your score isn't too bad, but you have to improve your score!")
elif m_score < 90 or e_score < 90:
    print('You need to improve, the score is bad. You will get a punishment.')
