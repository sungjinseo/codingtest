package com.example.lotto;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static java.util.stream.Collectors.toList;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

@SpringBootTest
class LottoApplicationTests {

    @Test
    void 로또당첨기생성_test(){
        //given
        //로또번호는 1~45까지만 생성되며 6개 숫자로 이뤄지고 행운번호는 1개이다
        //예외테스트는 따로 만드나?
        String lotto_numbers = "4,5,6,7,8,9";
        List<Integer> list_lotto =  Arrays.asList(4,5,6,7,8,10);
        String lucky_number = "15";

        //when
        Lotto lotto = new Lotto(lotto_numbers, lucky_number);

        //then

        assertEquals(6,lotto.getWinningResult(list_lotto));
    }

    @Test
    void 난수만들기_중복제거버전_test(){
        //given
        List<Integer> rtn_list = new ArrayList<>();
        int min_num = 1;
        int max_num = 45;
        int num_cnt = 6;
        int[] arr_num = new int[num_cnt];

        //when
        Random ran = new Random();
        while(rtn_list.size() != 6){
            int num = ran.nextInt(max_num) + min_num;
            if(rtn_list.contains(num)) continue;
            rtn_list.add(num);
        }

        assertEquals(rtn_list.size(), num_cnt);

        for(Integer item : rtn_list){
            assertFalse(item > max_num,"Error, item is too high" );
            assertFalse(item < min_num,"Error, item is too low");
        }


    }

    @Test
    void 랜덤으로만들기_test() {
        //given
        int min_num = 1;
        int max_num = 45;
        int num_cnt = 6;

        //when
        List<Integer> rtn_list = Arrays.stream(new Random().ints(num_cnt, min_num, max_num).toArray())
                .boxed()
                .collect(toList());

        //then
        assertEquals(rtn_list.size(), num_cnt);

        for(Integer item : rtn_list){
            assertFalse(item > max_num,"Error, item is too high" );
            assertFalse(item < min_num,"Error, item is too low");
        }

    }


    @Test
    void 스트림으로난수만들기_test(){
        //given
        List<Integer> rtn_list = new ArrayList<>();
        int min_num = 1;
        int max_num = 45;
        int num_cnt = 6;

        //when
        IntStream is = new Random().ints(min_num, max_num + 1);
        is.limit(num_cnt).forEach(rtn_list::add);

        //then
        assertEquals(rtn_list.size(), num_cnt);

        for(Integer item : rtn_list){
            assertFalse(item > max_num,"Error, item is too high" );
            assertFalse(item < min_num,"Error, item is too low");
        }
    }

    @Test
    void RANDOM_INTS_난수생성기_test(){
        //given
        int min_num = 1;
        int max_num = 45;
        int num_cnt = 6;

        //when
        List<Integer> rtn_list = new ArrayList<>();
        new Random().ints(min_num, max_num + 1).limit(num_cnt).forEach(rtn_list::add);

        //then
        assertEquals(rtn_list.size(), num_cnt);

        for(Integer item : rtn_list){
            assertFalse(item > max_num,"Error, item is too high" );
            assertFalse(item < min_num,"Error, item is too low");
        }

    }

}
