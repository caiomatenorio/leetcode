import java.util.HashMap;
import java.util.Map;

public class Solution {

    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int currentIndex = 0; currentIndex < nums.length; currentIndex++) {
            int complement = target - nums[currentIndex];
            Integer complementIndex = map.get(complement);

            if (complementIndex != null)
                return new int[] { complementIndex, currentIndex };

            map.put(nums[currentIndex], currentIndex);
        }

        throw new IllegalArgumentException("No solution found.");
    }

}
