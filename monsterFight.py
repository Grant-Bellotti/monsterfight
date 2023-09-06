class Monster():
    def __init__(self, name,  hp=20, type="Normal"):
        self.name = name
        self.type = type
        self.exp = 0
        self.current_hp = hp
        self.max_hp = hp
        self.attacks = {"wait":0}
        self.possible_attacks = {
    	    "sneak_attack": 1,
    	    "slash": 2,
    	    "ice_storm": 3,
    	    "fire_storm": 3,
    	    "whirlwind": 3,
    	    "earthquake": 2,
    	    "double_hit": 4,
    	    "tornado": 4,
    	    "wait": 0}
        #your code here
    def add_attack(self, attack_name):
        if (attack_name in self.possible_attacks and not(attack_name in self.attacks)):
            if (len(self.attacks) > 3):
                sorted_attacks = dict(sorted(self.attacks.items(), key=lambda item: item[1]))
                first_key = list(sorted_attacks.keys())[0]
                alp_attacks = {}
                for j in sorted_attacks:
                    if sorted_attacks[j] == sorted_attacks[first_key]:
                        alp_attacks[j] = j
                alp_attacks = dict(sorted(alp_attacks.items()))
                next_key = list(alp_attacks.keys())[0]
                sorted_attacks.pop(next_key)
                sorted_attacks[attack_name] = self.possible_attacks[attack_name]
                self.attacks = sorted_attacks
                return True
            else:
                self.attacks[attack_name] = self.possible_attacks[attack_name]
                return True
        return False
    def remove_attack(self, attack_name):
        if attack_name in self.attacks and len(self.attacks) > 0:
            self.attacks.pop(attack_name)
            if(len(self.attacks) == 0):
                self.attacks["wait"] = 0
            return True
        return False
    def win_fight(self):
        self.exp += 5
        self.current_hp = self.max_hp
    def lose_fight(self):
        self.exp += 1
        self.current_hp = self.max_hp

def monster_fight(monster1, monster2):
    if (len(monster1.attacks) > 1 or len(monster2.attacks) > 1) or not("wait" in monster1.attacks) or not("wait" in monster2.attacks):
        round_num = 0
        monster1_list = []
        monster2_list = []

        monster1_attacks_damage = dict(sorted(monster1.attacks.items(), key=lambda item: item[1],reverse=True))
        monster2_attacks_damage = dict(sorted(monster2.attacks.items(), key=lambda item: item[1],reverse=True))

        monster1_attacks = {}
        monster2_attacks = {}

        temp_attack1 = []
        for i in range(len(monster1_attacks_damage)):
            temp_list = []
            temp_key = list(monster1_attacks_damage.keys())[i]
            for j in monster1_attacks_damage:
                if monster1_attacks_damage[j] == monster1_attacks_damage[temp_key]:
                    temp_list.append(j)
            temp_list.sort()
            temp_attack1.extend(temp_list)
        for i in temp_attack1:
            monster1_attacks[i] = monster1_attacks_damage[i]

        temp_attack2 = []
        for i in range(len(monster2_attacks_damage)):
            temp_list = []
            temp_key = list(monster2_attacks_damage.keys())[i]
            for j in monster2_attacks_damage:
                if monster2_attacks_damage[j] == monster2_attacks_damage[temp_key]:
                    temp_list.append(j)
            temp_list.sort()
            temp_attack2.extend(temp_list)
        for i in temp_attack2:
            monster2_attacks[i] = monster2_attacks_damage[i]
        while (monster1.current_hp > 0 and monster2.current_hp > 0):
            round_num += 1
            next_attack = list(monster1_attacks.keys())[(round_num-1)%(len(monster1_attacks))]
            monster2.current_hp -= monster1_attacks[next_attack]
            monster1_list.append(next_attack)
            if(monster2.current_hp <= 0):
                monster1.win_fight()
                monster2.lose_fight()
                return(round_num, monster1, monster1_list)
            next_attack = list(monster2_attacks.keys())[(round_num-1)%(len(monster2_attacks))]
            monster1.current_hp -= monster2_attacks[next_attack]
            monster2_list.append(next_attack)
            if(monster1.current_hp <= 0):
                monster2.win_fight()
                monster1.lose_fight()
                return(round_num, monster2, monster2_list)
    else:
        return(-1, None, None)
