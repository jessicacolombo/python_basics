class Movie:

    def __init__(self, title: str, lenght: int):
        self.title = title
        self.length = lenght
        self.exibition_times = 0

    def __repr__(self) -> str:
        return f"Filme: {self.title}"

    def __len__(self) -> int:
        return self.length

    def __call__(self) -> int:
        self.exibition_times += 1
        return self.exibition_times


john_wick = Movie("John Wick", 113)

# 2
print(john_wick)

# 3
print(len(john_wick))

# 4
print(john_wick.exibition_times)

# 5
print(vars(john_wick))

# 6
john_wick()
print(john_wick.exibition_times)

# 7
print(vars(john_wick))
