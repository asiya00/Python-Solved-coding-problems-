class Donor:
    def __init__(self, Donor_ID, donor_name, contact_no, bloodgroup, PrevDonatedMon, AwayFrom):
        self.Donor_ID = Donor_ID
        self.donor_name = donor_name
        self.contact_no = contact_no
        self.bloodgroup = bloodgroup
        self.PrevDonatedMon = PrevDonatedMon
        self.AwayFrom = AwayFrom


class Bloodbank:
    def __init__(self, name, ListOfDonors):
        self.name = name
        self.ListOfDonors = ListOfDonors

    def getListofAvailableDonors():
        months = ["Jan", "Feb", "Mar", "Apr", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov"]
        di = {}



if __name__ == "__main__":
    t = int(input())
    ListOfDonors = []
    for i in range(t):
        Donor_ID = int(input())
        donor_name = input()
        contact_no = int(input())
        bloodgroup = input()
        PrevDonatedMon = input()
        AwayFrom = int(input())
        d = Donor(Donor_ID, donor_name, contact_no, bloodgroup, PrevDonatedMon, AwayFrom)
        ListOfDonors.append(d)
    blood_group = input()
    count_of_donors = int(input())
