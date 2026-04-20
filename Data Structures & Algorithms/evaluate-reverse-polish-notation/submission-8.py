class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []

        for token in tokens:
            # if token.isdigit():
            #     numbers.append(int(token))
            # else:
            if token == "-":
                number1, number2 = numbers.pop(), numbers.pop()
                numbers.append(number2 - number1)
            elif token == "+":
                number1, number2 = numbers.pop(), numbers.pop()
                numbers.append(number1 + number2)
            elif token == "*":
                number1, number2 = numbers.pop(), numbers.pop()
                numbers.append(number2 * number1)
            elif token == "/":
                number1, number2 = numbers.pop(), numbers.pop()
                numbers.append(int(float(number2) / number1))
            else:
                numbers.append(int(token))

        return numbers[0]


            

