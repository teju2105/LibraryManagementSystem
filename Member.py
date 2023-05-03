class Member:

    MEMBERS_FILE = 'members.txt'

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"<Member '{self.first_name} {self.last_name}'>"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    @staticmethod
    def get_all_members():
        members = []
        with open('Members.txt', 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                member = Member(parts[0], parts[1])
                members.append(member)
        return members

    @classmethod
    def add_member(cls, first_name, last_name):
        new_member = cls(first_name, last_name)
        with open(cls.MEMBERS_FILE, 'a') as file:
            file.write(f"{new_member.first_name},{new_member.last_name}\n")
        return new_member

    @classmethod
    def delete_member(cls, first_name, last_name):
        members = cls.get_all_members()
        with open(cls.MEMBERS_FILE, 'w') as file:
            for member in members:
                if member.first_name != first_name or member.last_name != last_name:
                    file.write(f"{member.first_name},{member.last_name}\n")
        return f"Member {first_name} {last_name} deleted successfully"
