impl Solution {
    pub fn running_sum(nums: Vec<i32>) -> Vec<i32> {
        let mut output = Vec::new();
        output.push(nums[0]);
        for x in 1..nums.len(){
            output.push(nums[x] + output[x-1]);
        }
        return output;
    }
}