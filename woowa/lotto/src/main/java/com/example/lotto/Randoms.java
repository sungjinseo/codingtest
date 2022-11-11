package com.example.lotto;

import java.security.SecureRandom;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;
import java.util.stream.IntStream;
import java.util.stream.Stream;

import static java.util.stream.Collectors.toList;

public class Randoms {

    public static List<Integer> pickUniqueNumbersInRange(int min_num, int max_num, int num_cnt){
        List<Integer> rtn_list = new ArrayList<>();
        Random ran = new Random();

        while(rtn_list.size() != num_cnt){
            int num = ran.nextInt(max_num) + min_num;
            if(rtn_list.contains(num)) continue;
            rtn_list.add(num);
        }
        return rtn_list;
    }
}
