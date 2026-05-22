class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string)) + "#" + string
        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        curr_pos = 0
        new_word = ""
        decoded_strs = []
        while curr_pos < len(s):
            delimiter_pos = s.index('#', curr_pos)
            length = s[curr_pos:delimiter_pos]
            for i in range(int(length)):
                new_word = s[delimiter_pos+1 : delimiter_pos+1+int(length)]
            decoded_strs.append(new_word)
            curr_pos = delimiter_pos + 1 + int(length)
            new_word = ""
        return decoded_strs

