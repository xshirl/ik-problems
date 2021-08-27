def letterCasePermutation(self, s: str) -> List[str]:
  result = []
  def helper(S, i, string):
      if i == len(S):
          result.append(string)
      else:
          if S[i].isdigit():
              helper(S, i+1, string + S[i])
          else:
              helper(S, i+1, string+ S[i].upper())
              helper(S, i+1, string + S[i].lower())
          
  helper(s, 0, "")
  return result