"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    """
    >>> output_all_items([1, 'hello', 'true'])
    1
    hello
    true

     """
    for item in items:
        print(item)
    


def get_all_evens(nums):
    """
    >>> get_all_evens([7, 8, 10, 1, 2, 2])
    [8, 10, 2, 2]

    """
    even_nums = []
    for num in nums:
        if num%2==0:
            even_nums.append(num)
    return even_nums

def get_odd_indices(items):
    """
    >>> get_odd_indices([1, 'hello', True, 500])
    ['hello', 500]

    """

    results = []

    for i in range(len(items)):
        if i % 2 !=0:
            results.append(items[i])

    return results



def print_as_numbered_list(items):
    """
    >>> print_as_numbered_list([1, 'hello', True])
    1. 1
    2. hello
    3. True
    
    """
    i = 1
    for item in items:
        print(f"{i}. {item}")
        i+=1

# print(print_as_numbered_list([1, 'hello', True]))

def get_range(start, stop):
    """
    >>> get_range(0, 5)
    [0, 1, 2, 3, 4]
    
    """
    result = []
    for i in range(start, stop):
        result.append(i)

    return result
    


def censor_vowels(word):
    """
    >>> censor_vowels('hello world')
    'h*ll* w*rld'
    """
    chars = []
    vowels = "aeiou"

    for letter in word:
        if letter in vowels:
            chars.append("*")
        else:
            chars.append(letter)
    return "".join(chars)


def snake_to_camel(string):

    """
    >>> snake_to_camel('hello_world')
    'HelloWorld'
    """
    
    words = string.split("_")
    result = []

    for i in range(len(words)):
        result.append(words[i].title())
    return "".join(result)


def longest_word_length(words):
    """
    >>> longest_word_length(['hello', 'world'])
    5
    """
    longest = len(words[0])
    for word in words:
        if len(word) > longest:
            longest = len(word)
    return longest


def truncate(string):
    """
    >>> truncate('aaaabbbbcccca')
    abca
    """
    # string = set(string)
    result = [] #a
    result.append(string[0]) 
    string.pop(0)
    for i in range(len(string)):
        # if string[i] == string[i + 1]:
 
        if i != result[i - 1]:
            result.append(i)


    return result


# def has_balanced_parens(string):

#     """
#     >>> hasBalancedParens('((This) (is) (good))')
#     true
#     """
#     pass  # TODO: replace this line with your code


# def compress(string):
#     """ 
#     >>> compress('Hello, world! Cows go moooo...')
#     Hel2o, world! Cows go mo4.3
#     """
#     pass  # TODO: replace this line with your code
