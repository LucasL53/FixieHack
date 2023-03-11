import random

import fixieai
import uwtools

BASE_PROMPT = """I'm an agent that rolls virtual dice!"""
FEW_SHOTS = """
Q: Roll a d20
Ask Func[roll]: 20 1
Func[roll] says: 12
A: You rolled a 12!

Q: Roll two dice and blow on them first for good luck
Ask Func[roll]: 6 2
Func[roll] says: 4 3
A: You rolled a 4 and a 3, with a total of 7.

Q: Roll 3d8
Ask Func[roll]: 8 3
Func[roll] says: 5 3 8
A: You rolled 5, 3, and 8, for a total of 16.

Q: Show the description of CSE133
Ask Func[get_class_information]: CSE133 Description
Func[get_class_information] says: Intermediate data programming. Topics include writing programs that manipulate different types of data; leveraging the growing ecosystem of tools and libraries for data programming; writing programs that are both efficient and elegant; and writing medium-scale programs (100 to 200 lines). Prerequisite: either CSE 122, CSE 123, CSE 142, CSE 143, or CSE 160.
A: Here is the description of CSE133: Intermediate data programming. Topics include writing programs that manipulate different types of data; leveraging the growing ecosystem of tools and libraries for data programming; writing programs that are both efficient and elegant; and writing medium-scale programs (100 to 200 lines). Prerequisite: either CSE 122, CSE 123, CSE 142, CSE 143, or CSE 160.

Q: Give me the description of CSE163
Ask Func[get_class_information]: CSE163 Description
Func[get_class_information] says: Intermediate data programming. Topics include writing programs that manipulate different types of data; leveraging the growing ecosystem of tools and libraries for data programming; writing programs that are both efficient and elegant; and writing medium-scale programs (100 to 200 lines). Prerequisite: either CSE 122, CSE 123, CSE 142, CSE 143, or CSE 160.
A: Here is the description of CSE163: Intermediate data programming. Topics include writing programs that manipulate different types of data; leveraging the growing ecosystem of tools and libraries for data programming; writing programs that are both efficient and elegant; and writing medium-scale programs (100 to 200 lines). Prerequisite: either CSE 122, CSE 123, CSE 142, CSE 143, or CSE 160.

Q: What are the prerequisites of CSE400
Ask Func[get_class_information]: CSE400 Prerequisites
Func[get_class_information] says: CSE122,CSE123,CSE142,CSE143,CSE160
A: Here are the prerequisites of CSE400: CSE122,CSE123,CSE142,CSE143,CSE160

Q: How many credits is LING200?
Ask Func[get_class_information]: LING200 Credits
Func[get_class_information] says: 5
A: LING200 is a 5 credits class.

"""
agent = fixieai.CodeShotAgent(BASE_PROMPT, FEW_SHOTS)


@agent.register_func
def roll(query: fixieai.Message) -> str:
    dsize, num_dice = query.text.split()
    dice = [random.randint(1, int(dsize)) for _ in range(int(num_dice))]
    return " ".join([str(x) for x in dice])


course_catalog_dict = {}


@agent.register_func
def get_class_information(query: fixieai.Message) -> str:
    global course_catalog_dict
    class_code, category = query.text.split()
    if not course_catalog_dict:
        course_catalog_dict = uwtools.course_catalogs(struct='dict')

    return course_catalog_dict[class_code][category]
