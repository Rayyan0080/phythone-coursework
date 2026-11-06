def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
        n = int(lines[0].strip())
        edges = [tuple(map(int, line.strip().split())) for line in lines[1:]]
        return n, edges
    except FileNotFoundError:
        return None, None

def calculate_statistics(n, edges):
    friends = [0] * n
    for u, v in edges:
        if u < n:
            friends[u] += 1
        if v < n:
            friends[v] += 1

    max_friends = max(friends)
    avg_friends = sum(friends) / n
    max_friend_ids = [i for i in range(n) if friends[i] == max_friends]

    return friends, max_friends, avg_friends, max_friend_ids

def recommend_friend(user_id, n, edges):
    def common_friends_count(a, b):
        a_friends = [v for u, v in edges if u == a] + [u for u, v in edges if v == a]
        b_friends = [v for u, v in edges if u == b] + [u for u, v in edges if v == b]
        a_friends.sort()
        b_friends.sort()
        common = []
        i = j = 0
        while i < len(a_friends) and j < len(b_friends):
            if a_friends[i] == b_friends[j]:
                common.append(a_friends[i])
                i += 1
                j += 1
            elif a_friends[i] < b_friends[j]:
                i += 1
            else:
                j += 1
        return len(common), common

    user_friends = [v for u, v in edges if u == user_id] + [u for u, v in edges if v == user_id]
    user_friends.sort()

    max_common = -1
    best_friend = -1
    for friend in range(n):
        if friend != user_id and friend not in user_friends:
            common_count, _ = common_friends_count(user_id, friend)
            if common_count > max_common:
                max_common = common_count
                best_friend = friend

    if max_common > 0:
        return best_friend, max_common
    else:
        return None, 0

def common_friends_list(user1, user2, edges):
    user1_friends = [v for u, v in edges if u == user1] + [u for u, v in edges if v == user1]
    user2_friends = [v for u, v in edges if u == user2] + [u for u, v in edges if v == user2]
    user1_friends.sort()
    user2_friends.sort()

    common = []
    i = j = 0
    while i < len(user1_friends) and j < len(user2_friends):
        if user1_friends[i] == user2_friends[j]:
            common.append(user1_friends[i])
            i += 1
            j += 1
        elif user1_friends[i] < user2_friends[j]:
            i += 1
        else:
            j += 1
    return common

def main():
    while True:
        file_name = input("Enter the name of the file: ")
        n, edges = read_file(file_name)
        if n is None:
            print("There is no file with that name. Try again.")
        else:
            break

    friends, max_friends, avg_friends, max_friend_ids = calculate_statistics(n, edges)
    print("\nFirst general statistics about the social network:\n")
    print(f"This social network has {n} people/users.")
    print(f"In this social network the maximum number of friends that any one person has is {max_friends}.")
    print(f"The average number of friends is {avg_friends}.")
    print(f"There are {len(max_friend_ids)} people with {max_friends} friends and here are their IDs: {' '.join(map(str, max_friend_ids))} \n")

    import random
    random_num = random.randint(0, max_friends)
    print("I now pick a number at random.")
    print(f"That number is: {random_num}. Let's see how many people has that many friends.")
    count_random_friends = sum(1 for f in friends if f >= random_num)
    print(f"There is {count_random_friends} people with {random_num} or more friends\n")

    knows_everyone = any(f == n - 1 for f in friends)
    if knows_everyone:
        print("There at least one person that knows everyone.\n")
    else:
        print("There is nobody that knows everyone.\n")

    print("We are now ready to recommend a friend for a user you specify.")
    while True:
        try:
            user_id = int(input("Enter an integer for a user ID:"))
            if user_id < 0 or user_id >= n:
                print("That user ID does not exist. Try again.")
            else:
                break
        except ValueError:
            print("That was not an integer. Please try again.")

    best_friend, common_count = recommend_friend(user_id, n, edges)
    if best_friend is not None:
        print(f"For user with ID {user_id} we recommend the user with ID {best_friend}")
        print(f"That is because users {user_id} and {best_friend} have {common_count} common friends and")
        print(f"user {user_id} does not have more common friends with anyone else.\n")
    else:
        print(f"We have nobody to recommend for user with ID {user_id} since he/she is dominating in their connected component\n")

    print("Finally, you showed interest in knowing common friends of some pairs of users.")
    print("About 1st user ...")
    while True:
        try:
            user1 = int(input("Enter an integer for a user ID:"))
            if user1 < 0 or user1 >= n:
                print("That user ID does not exist. Try again.")
            else:
                break
        except ValueError:
            print("That was not an integer. Please try again.")

    print("About 2st user ...")
    while True:
        try:
            user2 = int(input("Enter an integer for a user ID:"))
            if user2 < 0 or user2 >= n:
                print("That user ID does not exist. Try again.")
            else:
                break
        except ValueError:
            print("That was not an integer. Please try again.")

    common = common_friends_list(user1, user2, edges)
    if common:
        print(f"Here is the list of common friends of {user1} and {user2}")
        print(" ".join(map(str, common)), "\n")
    else:
        print(f"{user1} and {user2} have no common friends.\n")

if __name__ == "__main__":
    main()
