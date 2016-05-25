import re

# strings = (r'these', r"are", r'''all''', r"""strings""")
# r = indication of a raw string literal (interpret backslashes as literal backslashes)

# string = r'\n \t \b ' 
# print(string == '\\n \\t \\b ')
# match_start_of_string = r'^'

#Gives blank - matches start of string 
x0 = re.match(r'^', 'az09_&^%$\nfoo').group()
#matches end of string 
# r('$')

#Gives 'a'
x1 = re.match(r'.', 'az09_&^%$\nfoo').group()

# Gives az09_&^%$ because * matches for zero or more times
x2 = re.match(r'.*', 'az09_&^%$\nfoo').group()

# Gives everything in the string including foo because of dotall
x3 = re.match(r'.*', 'az09_&^%$\nfoo', re.DOTALL).group()

x4 = re.match(r'.*', 'az09_&^%$\nfoo', re.DOTALL | re.MULTILINE).group()
# print(x0)


# Will match as many as possible by default 
match_zero_or_more_repetitions = r'*' 
match_one_or_more_repetitions = r'+'
match_zero_or_one_repetitions = r'?'
match_5_repetitions = r'{5}'
match_5_to_7_repetitions = r'{5,7}'
match_zero_or_more_repetitions_of_a = r'a*'
match_5_to_7_repetitions_of_a = r'a{5,7}'

# print(re.match(match_zero_or_more_repetitions_of_a, 'aaaaaaabcdefghijkl').group())


#matching strings
match_lowercase_alphabet = r'[a-z]' # can define a range to match!
match_lowercase_vowels = r'[aeiou]' # matches any vowel once

# Should be able to match any string beginning to end so long as there's no new line
sample_pattern = r'^.*$'

test_string = 'foo bar baz'
result_match_object = re.match(sample_pattern, test_string)

#without specifying .group() you'll just get a MatchObject
# print(result_match_object.group())

test_string2 = 'foo \n bar \n baz'
result_None = re.match(sample_pattern, test_string2, re.M | re.DOTALL)
# print(result_None.group())

# can also use re.search, re.findall()
result_None = re.findall(sample_pattern, test_string2, re.M | re.DOTALL)
# print(result_None)

finditer_results = re.finditer(sample_pattern, test_string2, re.M)
#for i in finditer_results: 
    # print(i.group()) # prints each line as shown in prior list.

txt1 = '''You can reach us at 555.867.5309, or email us at a.b.c234@mta.info.com'''
txt2 = '''Contact us at (555) 123-0987''' 

phone_matcher = re.compile(
    r'''
    (\d{3}) # match any three numbers (the parentheses indicate it's a capture group)
    .*?     # followed by an minimal amount of characters to match the rest 
    (\d{3}) # followed by 3 numbers (a capture group)
    [-.]  # followed by a dash, period, or whitespace
    (\d{4}) # followed by 4 numbers (another capture group)
    ''',
    flags=re.VERBOSE | re.DOTALL)

results = []
for txt in (txt1, txt2):
	result = phone_matcher.search(txt)
	if result is not None:
		results.append(result.groups())


print(results)










