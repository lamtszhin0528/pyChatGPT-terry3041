import openai

openai_api_key = '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' #gjgold702@gmail.com'
max_tokens = 2048
gpt_mode = 'gpt-4'

openai.api_key = openai_api_key

def ask (text) :

    response = openai.ChatCompletion.create(
        # engine=model,
        # prompt=text,
        model = gpt_mode,
        messages=[
            {"role": "system", "content": "Assistant is a large language model trained by OpenAI and it can possess strong financial and cryptocurrency analysis capabilities"},
            {"role": "user", "content": text}
        ],
        max_tokens=int(max_tokens)
    )

    answer = response.choices[0].message['content'].strip()
    toekn_used = response.usage
    # print (toekn_used)
    # Return the answer as a JSON object
    return (answer,toekn_used)

if __name__ == '__main__':
    question = ''
    while True:
        text = input('You: ')
        if not text == '!!' : 
            question += text
            continue
        else :
            answer , toekn_used = ask(question)
            question = ''
        print ('\ntoken used: ' + str(toekn_used))
        print ('===='*4)
        print('\nBot: ' + answer )
