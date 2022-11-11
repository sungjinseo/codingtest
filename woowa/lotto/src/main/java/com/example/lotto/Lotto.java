package com.example.lotto;

import java.util.ArrayList;
import java.util.List;

public class Lotto {
    public final static int MIN_LOTTO_NUM = 1;
    public final static int MAX_LOTTO_NUM = 45;
    public final static int LOTTO_NUMBER_CNT = 6;

    private final static int LOTTO_LUCK_CNT = 1;
    private final static String SEPERATE_CHAR = ",";
    private final List<Integer> numbers;
    private final int lucky_number;

    public Lotto(String numbers, String lucky_number) {
        String[] arr_str_num = numbers.split(SEPERATE_CHAR);
        if(arr_str_num.length != LOTTO_NUMBER_CNT) throw new IllegalArgumentException("[ERROR] 로또당첨번호는 6개입니다.");
        List<Integer> num_list = getNumberList(numbers);

        this.numbers = num_list;
        this.lucky_number = this.exchangeDigit(lucky_number);
    }

    private int exchangeDigit(String numbers){
        int number = 0;
        try{
            number = Integer.parseInt(numbers);
            if (number < MIN_LOTTO_NUM || number > MAX_LOTTO_NUM){
                throw new IllegalArgumentException("[ERROR] 로또 번호는 1부터 45 사이의 숫자여야 합니다.");
            }
        }catch (IllegalArgumentException e){
            throw new IllegalArgumentException("[ERROR] 로또 번호는 1부터 45 사이의 숫자여야 합니다.");
        }
        return number;
    }
    private List<Integer> getNumberList(String numbers){
        String[] arr_num = numbers.split(",");
        List<Integer> rtn_list = new ArrayList<>();

        for(int i=0; i<arr_num.length; i++){
            rtn_list.add(exchangeDigit(arr_num[i]));
        }
        return rtn_list;
    }

    public int getWinningResult(List<Integer> ticket){
        int winning_cnt = (int)ticket.stream().map(item->this.numbers.contains(item) ? 1:0).reduce(0 , Integer::sum);

        if(winning_cnt < 6){

        }

        return winning_cnt;
    }
}