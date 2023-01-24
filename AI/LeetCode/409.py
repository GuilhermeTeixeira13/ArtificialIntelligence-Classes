class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Criar dicionário com elementos do tipo letra -> número de letras na palavra

        letters = {}
        for char in s:
            if char not in letters:
                letters[char] = 1
            else:
                letters[char] += 1

        res = 0
        odd = 0

        if len(letters) == 1:
            return letters[s[0]]

        # Contabilizar números pares e ímpares para cálculo do resultado
        for i in letters.values():
            if i > 1:
                if i % 2 == 0:
                    res += i
                else:
                    res += i - 1
                    odd += 1
            else:
                odd += 1

        # Se houver mais do que um ímpar, podemos adicionar essa letra ao palíndromo
        if odd >= 1:
            res += 1

        return res
