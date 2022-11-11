package com.example.lotto;

import java.security.SecureRandom;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Randoms {

    public static List<Integer> pickUniqueNumbersInRange(int str_num, int end_num, int num_cnt){

        List<Integer> rtn_list = new ArrayList<>();

        while(rtn_list.size() == num_cnt){
            Random rand = new Random();
            rtn_list.add((int)rand.nextInt(end_num)+1);
        }

        System.out.println("============================================item");
        for(Integer item : rtn_list){
            System.out.println(item);
        }

//        for(int i=0; i<num_cnt; i++){
//
//            rtn_list.add((int) ((Math.random() * (end_num - str_num)) + str_num));
//        }

        return rtn_list;
    }
}
