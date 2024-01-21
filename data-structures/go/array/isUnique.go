package array

import (
	"fmt"
)

// Implement an algorithm to determine if an array has all unique characters;
// uses Hash table, O(n)
func isUnique_hashtable(array []int) bool {
	hash_table := make(map[int]bool)

	for _, i := range array {
		if _, exists := hash_table[i]; exists {
			return false
		}
		hash_table[i] = true
	}
	return true
}

// Implement an algorithm to determine if an array has all unique characters;
// uses Brute Force, O(n^2)
func isUnique_BruteForce(array []int) bool {
	for i := 0; i < len(array) - 1; i++ {
		for j := i + 1; j < len(array); j++ {
			if array[i] == array[j] {
				return false
			}
		}
	}
	return true
}

// Given an array, check if it contains only unique characters
func RunIsUnique() {
	fmt.Println("Brute Force:")
	fmt.Println(isUnique_BruteForce([]int{1, 2, 3, 4, 1}))
	fmt.Println(isUnique_BruteForce([]int{0, 0, 0, 0}))
	fmt.Println(isUnique_BruteForce([]int{1, 2, 1}))
	fmt.Println(isUnique_BruteForce([]int{1, 2, 3, 4}))
	fmt.Println(isUnique_BruteForce([]int{}))
	fmt.Println("\nHash Table:")
	fmt.Println(isUnique_hashtable([]int{1, 2, 3, 4, 1}))
	fmt.Println(isUnique_hashtable([]int{0, 0, 0, 0}))
	fmt.Println(isUnique_hashtable([]int{1, 2, 1}))
	fmt.Println(isUnique_hashtable([]int{1, 2, 3, 4}))
	fmt.Println(isUnique_hashtable([]int{}))
}