import heapq,os

class BinaryTree:
    def __init__(self,value,frequ):
        self.value = value
        self.frequ = frequ
        self.left = None
        self.right = None

class Huffmancode:
    def __init__(self,path):
        self.path = path
        self.__heap = []
        self.__code = []


    def __lt__(self,other):  
        return self.frequ < other.frequ
    

    def __eq__(self,other):
        return self.frequ == other.frequ
    

    def __frequency_from_text(self,text): 
        frequ_dict = {}
        for char in text:
            if char not in frequ_dict:
                frequ_dict[char] = 0
            frequ_dict[char] +=1
        return frequ_dict 


    def __Build_heap(self,frequency_dict):
        for key in frequency_dict:
            frequency = frequency_dict[key]
            binary_tree_node = BinaryTree(key,frequency)
            heapq.heappush(self.__heap , binary_tree_node)


    def __Build_Binary_Tree(self):
     while len(self.__heap ) > 1:
        binary_tree_node_1 = heapq.heappop(self.__heap)
        binary_tree_node_2 = heapq.heappop(self.__heap)
        sum_of_freq = binary_tree_node_1.frequ + binary_tree_node_2.frequ
        newnode = BinaryTree(None,sum_of_freq)
        newnode.left = binary_tree_node_1
        newnode.right = binary_tree_node_2
        heapq.heappush(self.__heap,newnode)
     return
    

    def __Build_Tree_Code_Helper(self,root,curr_bits):
            if root is None:
                return
            if root.value is not None:
                self.__code[root.value] = curr_bits
                return
            self.__Build_Tree_Code_Helper(root.left,curr_bits+'0')
            self.__Build_Tree_Code_Helper(root.right,curr_bits+'1')


    def __Build_Tree_Code(self):
        root = heapq.heappop(self.__heap)
        self.__Build_Tree_Code_Helper(root,'')


    def __Build_Encoded_Text(self,text):
        encoded_text = ''
        for char in text:
            encoded_text += self.__code[char]

        return encoded_text


    def __Build_Padded_Text(self,encoded_text):
        padding_value = 8 - len(encoded_text) % 8
        for i in range(padding_value):
            encoded_text == '0'

        padded_info = "{0.08b}".format(padding_value)
        padded_text = padded_info + padded_text
        return padded_text

    def __Build_Bite_Array(self,padded_text):
        array = []
        for i in range(0,len(padded_text),8):
           byte = padded_text[i:i+8]
           array.append(int(byte,2))
        return array      
    

    def compression(self):
        print("COMPRESSION started.")
        #to access the file and extract text from the file
        filename,file_extension = os.path.splitext(self.path)
        output_path = filename + '.bin'
        with open(self.path, 'r+') as file , open(output_path,'wb') as output:
            text = file.read()
            text = text.rstrip()
        frequency_dict = self.__frequency_from_text(text)
        #calculate the frequency of each text and store it in frequency dictionary
        build_heap = self.__Build_heap(frequency_dict)
        #min heap for two min frequencies
        #use the min heap and construct a binary tree
        self.__Build_Binary_Tree()
        #construct codes from binary tree and store it in dictionary
        self.__Build_Tree_Code()
        #constructing encoded text
        encode_text = self.__Build_Encoded_Text(text)
        #padding of encoded text
        padded_text = self.__Build_padded_Text(encode_text)
        #return the encoded text
        bytes_array = self.__Build_Bite_Array(padded_text)
        final_bytes = bytes(bytes_array)
        output.write(final_bytes)
        print('compressed successfully')
        return output_path 


path = input("Enter the path of file: ")
h = Huffmancode(path)
h.compression()