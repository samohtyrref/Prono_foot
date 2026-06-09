import sys
import random

country_list = [["Canada", 30],
                ["Etats_Unis", 17],
                ["Mexique", 14],
                ["Arabie_saoudite", 61],
                ["Australie", 27],
                ["Irak", 56],
                ["Japon", 18],
                ["Jordanie", 63],
                ["Ouzbekistan", 50],
                ["Qatar", 57],
                ["Republique_de_Coree", 120],
                ["RI_Iran", 20],
                ["Afrique_du_Sud", 60],
                ["Algerie", 28],
                ["Cap_Vert", 67],
                ["Cote_d_Ivoire", 33],
                ["Egypte", 29],
                ["Ghana", 73],
                ["Maroc", 7],
                ["RD_Congo", 45],
                ["Senegal", 15],
                ["Tunisie", 46],
                ["Curacao", 82],
                ["Haiti", 83],
                ["Panama", 34],
                ["Argentine", 1],
                ["Bresil", 6],
                ["Colombie", 13],
                ["Equateur", 23],
                ["Paraguay", 40],
                ["Uruguay", 16],
                ["Nouvelle_Zelande", 85],
                ["Allemagne", 10],
                ["Angleterre", 4],
                ["Autriche", 24],
                ["Belgique", 9],
                ["Bosnie_Herzegovine", 64],
                ["Croatie", 11],
                ["Ecosse", 42],
                ["France", 3],
                ["Espagne", 2],
                ["Norvege", 31],
                ["Pays-Bas", 8],
                ["Portugal", 5],
                ["Suede", 38],
                ["Suisse", 19],
                ["Tchequie", 39],
                ["Turquie", 22]]

def rotate_score(score1, score2):
    return score2, score1

def get_score(team1, team2):
    team_power1 = 0.0
    team_power2 = 0.0
    score_team1 = 0
    score_team2 = 0
    for country in country_list:
        if( team1 == country[0]):
            team_power1 = (61 - country[1])/100
        if( team2 == country[0]):
            team_power2 = (61 - country[1])/100

    deviation = (team_power1 - team_power2)*5 + 1
    score_team1 = abs(int(random.normalvariate( mu = 1 , sigma = deviation)))
    score_team2 = abs(int(random.normalvariate( mu = 1 , sigma = deviation)))
    if(team_power1 > team_power2):
        if(score_team1 < score_team2):
            score_team1, score_team2 = rotate_score(score_team1,score_team2)
    elif(team_power2 > team_power1):
        if(score_team2 < score_team1):
            score_team1, score_team2 = rotate_score(score_team1,score_team2)

    return score_team1, score_team2

def main():
    score1, score2 = get_score(sys.argv[1], sys.argv[2])
    print( str(score1) + " - " + str(score2) )

if __name__ == "__main__":
    main()

