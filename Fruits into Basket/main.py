class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        start = max_fruits = 0

        for end, tree_type in enumerate(fruits, 0):
            if len(basket) < 2 and tree_type not in basket:
                basket[tree_type] = True
                max_fruits = max(max_fruits, end - start + 1)

            elif tree_type in basket:
                max_fruits = max(max_fruits, end - start + 1)

            else:
                basket = {}
                basket[fruits[end-1]] = True
                basket[tree_type] = True
                start = end - 1

                while fruits[start] == fruits[start-1]:
                    start -= 1

                max_fruits = max(max_fruits, end - start + 1)

        return max_fruits
