from questions import checkBalance

if __name__ == "__main__":
    number = int(input())
    for val in range(0, number):
        lst = list(str(input()).split())
        print(checkBalance(lst=lst, dictionary={"<": ">", "{": "}", "(": ")", "[": "]"}))
        # print(checkParanthesis(lst=lst))
