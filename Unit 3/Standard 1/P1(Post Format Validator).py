'''
Problem 1: Post Format Validator
You are managing a social media platform and need to ensure that posts are properly formatted. Each post must have balanced and correctly nested tags, such as () for mentions, [] for hashtags, and {} for links. You are given a string representing a post's content, and your task is to determine if the tags in the post are correctly formatted.

A post is considered valid if:

Every opening tag has a corresponding closing tag of the same type.
Tags are closed in the correct order.
def is_valid_post_format(posts):
  pass
Example Usage:

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))
Example Output:

True
True
False
'''

def is_valid_post_format(posts):
  stack = []
  for i in posts: 
    if i == "(" or i == "[" or i == "{":
      stack.append(i)
    if len(stack) != 0:
      if stack[-1] == "(" and i == ")":
        stack.pop()
      elif stack[-1] == "[" and i == "]":
        stack.pop()
      elif stack[-1] == "{" and i == "}":
        stack.pop()
  return True if len(stack) == 0 else False

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))