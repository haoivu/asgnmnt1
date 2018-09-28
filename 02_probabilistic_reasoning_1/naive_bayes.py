from collections import Counter


yes = "yes"
no = "no"

sky =       ["sunny", "sunny", "overcast", "rainy", "rainy", "rainy", "overcast", "sunny", "sunny", "rainy", "sunny", "overcast", "overcast", "rainy"]
temp =      ["hot", "hot", "hot", "mild", "cool", "cool", "cool", "mild", "cool", "mild", "mild", "mild", "hot", "mild"]
humidity =  ["high", "high", "high", "high", "normal", "normal", "normal", "high", "normal", "normal", "normal", "high", "normal", "high"]
wind =      [False, True, False, False, False, True, True, False, False, False, True, True, False, True]
play =      [no, no, yes, yes, yes, no, yes, no, yes, yes, yes, yes, yes, no]

dataset = [sky, temp, humidity, wind, play]

sky_set = [sky, play]

def check_set(input_set):
    set = [input_set, play]
    yay_counter = []
    yay = 0
    nay_counter = []
    nay = 0
    for j in range(len(input_set)):
        a = [i[j] for i in set]
        if a[1] == "yes":
            yay += 1
            yay_counter.append(a[0])
        else:
            nay += 1
            nay_counter.append(a[0])
    yay_counts = Counter(yay_counter)
    nay_counts = Counter(nay_counter)

    if input_set == sky:
        print("- SKY")
        play_sunny = float(yay_counts["sunny"]) / yay
        play_overcast = float(yay_counts["overcast"]) / yay
        play_rainy = float(yay_counts["rainy"]) / yay
        print("Probability of playing with sun:", play_sunny)
        print("Probability of playing with overcast:", play_overcast)
        print("Probability of playing with rain:", play_rainy)
        print("")
        _play_sunny = float(nay_counts["sunny"]) / nay
        _play_overcast = float(nay_counts["overcast"]) / nay
        _play_rainy = float(nay_counts["rainy"]) / nay
        print("Probability of NOT playing with sun:", _play_sunny)
        print("Probability of NOT playing with overcast:", _play_overcast)
        print("Probability of NOT playing with rain:", _play_rainy)
        print("--------------------------------------------------------------------")

    if input_set == temp:
        print("- TEMPERATURE")
        play_hot = float(yay_counts["hot"]) / yay
        play_mild = float(yay_counts["mild"]) / yay
        play_cool = float(yay_counts["cool"]) / yay
        print("Probability of playing when hot:", play_hot)
        print("Probability of playing when mild:", play_mild)
        print("Probability of playing when cool:", play_cool)
        print("")
        _play_hot = float(nay_counts["hot"]) / nay
        _play_mild = float(nay_counts["mild"]) / nay
        _play_cool = float(nay_counts["cool"]) / nay
        print("Probability of NOT playing when hot:", _play_hot)
        print("Probability of NOT playing when mild:", _play_mild)
        print("Probability of NOT playing when cool:", _play_cool)
        print("--------------------------------------------------------------------")

    if input_set == humidity:
        print("- HUMIDITY")
        play_high = float(yay_counts["high"]) / yay
        play_normal = float(yay_counts["normal"]) / yay
        print("Probability of playing when high:", play_high)
        print("Probability of playing when normal:", play_normal)
        print("")
        _play_high = float(nay_counts["high"]) / nay
        _play_normal = float(nay_counts["normal"]) / nay
        print("Probability of NOT playing when high:", _play_high)
        print("Probability of NOT playing when normal:", _play_normal)
        print("--------------------------------------------------------------------")

    if input_set == wind:
        print("- HUMIDITY")
        play_no_wind = float(yay_counts[False]) / yay
        play_wind = float(yay_counts[True]) / yay
        print("Probability of playing when no wind:", play_no_wind)
        print("Probability of playing when wind:", play_wind)
        print("")
        _play_no_wind = float(nay_counts[False]) / nay
        _play_wind = float(nay_counts[True]) / nay
        print("Probability of NOT playing when high:", _play_no_wind)
        print("Probability of NOT playing when normal:", _play_wind)
        print("--------------------------------------------------------------------")

    print("--------------------------------------------------------------------")

check_set(sky)
check_set(temp)
check_set(humidity)
check_set(wind)
