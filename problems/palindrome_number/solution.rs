impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        let str_x = x.to_string();
        let chars: Vec<char> = str_x.chars().collect();
        let len = chars.len();

        for i in 0..len / 2 {
            if chars[i] != chars[len - 1 - i] {
                return false;
            }
        }
        true
    }
}