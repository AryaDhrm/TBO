import gui
from data import *

# Function to perform the CYK Algorithm
def CYK(words, n):
    # Mengubah lhs aturan grammar menjadi huruf kecil
    # R_lower = {key.lower(): [[rule for rule in rules] for rules in rules_list] for key, rules_list in R.items()}

    # Inisialisasi tabel
    T = [[set([]) for _ in range(n)] for _ in range(n)]

    # Filling in the table
    for j in range(n):
        # Iterate over the rules
        for lhs, rule in R.items():
            for rhs in rule:
                # If a terminal is found
                if len(rhs) == 1 and rhs[0] == words[j]:
                    T[j][j].add(lhs)

        for i in range(j - 1, -1, -1):
            # Iterate over the range i to j + 1
            for k in range(i, j):
                # Iterate over the rules
                for lhs, rule in R.items():
                    for rhs in rule:
                        # If a terminal is found
                        if len(rhs) == 2 and rhs[0] in T[i][k] and rhs[1] in T[k + 1][j]:
                            T[i][j].add(lhs)

    # ... (sisa kode tetap tidak berubah)

    # If the sentence can be formed by rules of the given grammar
    if "K" in T[0][n - 1]:
        # print(T[0][n - 1])
        # print("AWAWA")
        gui.cek = 'rill'
        return T;
        # st.ballons()
        # print("False")
    else:
        gui.cek = 'fek'
        # print("True")

# Driver Code

# Given string (space-separated input)
# input_sentence = "ini terpanjang"
# input_sentence = input("masukan kalimat : ")
# words = input_sentence.split()
# print(words)
# words.split()
# Function Call
# global kata
# CYK(kata)

