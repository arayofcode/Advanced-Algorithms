package array

import (
	"fmt"
)

// Check length and character count using hash table;
// O(n)
func checkPermutation_Count(a string, b string) bool {
	if len(a) != len(b) {
		return false
	}

	hashTable := make(map[rune]int)
	for _, letter := range a {
		hashTable[letter]++
	}

	for _, letter := range b {
		hashTable[letter]--
	}

	for _, value := range hashTable {
		if value != 0 {
			return false
		}
	}
	return true
}

// Given two strings, check if one is permutation of other
func RunCheckPermutation() {
	fmt.Println(checkPermutation_Count("", ""))
	fmt.Println(checkPermutation_Count("a", ""))
	fmt.Println(checkPermutation_Count("", "a"))
	fmt.Println(checkPermutation_Count("a", "a"))
	fmt.Println(checkPermutation_Count("a", "ab"))
	fmt.Println(checkPermutation_Count("ba", "ab"))
	fmt.Println(checkPermutation_Count("baa", "bab"))
	fmt.Println(checkPermutation_Count("baa", "aab"))
	fmt.Println(checkPermutation_Count("baab", "aabb"))
}