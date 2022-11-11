package com.example.lotto;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.util.*;

@SpringBootApplication
public class LottoApplication {

    private final static int TICKET_AMT = 1000;
    public static Boolean isdigit(String num){
        char[] item_list = num.toCharArray();
        for(int i=0; i<item_list.length; i++){
            if(item_list[i] < 48 || item_list[i] > 57) return false;
        }

        return true;
    }

    public static void print(Object obj){
        System.out.println(obj);
    }

    public static void main(String[] args) {
        SpringApplication.run(LottoApplication.class, args);

        Scanner sc = new Scanner(System.in); // creates instance of Scanner to read from console
        print("구입금액을 입력해 주세요.");
        String str_amt = sc.nextLine();
        Boolean chk_amt = isdigit(str_amt);

        if(!chk_amt) throw new IllegalArgumentException();
        int int_amt = Integer.parseInt(str_amt);
        if(int_amt < 1000) throw new IllegalArgumentException();

        List<List<Integer>> lotto_ticket_list = new ArrayList<>();

        for(int i=0; i<int_amt/TICKET_AMT; i++){
            List<Integer> ticket = Randoms.pickUniqueNumbersInRange(Lotto.MIN_LOTTO_NUM, Lotto.MAX_LOTTO_NUM, Lotto.LOTTO_NUMBER_CNT);
            lotto_ticket_list.add(ticket);
        }

        print("8개를 구매했습니다.");
        for(List<Integer> item : lotto_ticket_list){
            print(item);
        }

        print("당첨 번호를 입력해 주세요.");
        String lotto_numbers = sc.nextLine();
        print("보너스 번호를 입력해 주세요.");
        String lucky_number = sc.nextLine();
        Lotto lotto = new Lotto(lotto_numbers, lucky_number);

        for(List<Integer> ticket : lotto_ticket_list){
            print(lotto.getWinningResult(ticket));
        }

        //Lotto lotto = new Lotto();
//        boolean bl = sc.nextBoolean(); // read boolean
//        String str = sc.nextLine(); // read string
//        System.out.println("integer = " + num + " boolean = " + bl + " string = " + "'" + str + "'");
//        sc.close(); // close scanner


    }



}
