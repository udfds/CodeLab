// ---------------------------------------------------------------------
// Functions
// ---------------------------------------------------------------------
function isEvenOrOdd(number) {
    return number % 2 ? 'Odd' : 'Even';
}

function findGreekSymbol(word) {
    let dictionary = {
        alfa: 'A', beta: 'B', gamma: 'Γ', delta: 'Δ', epsilon: 'E',
        zeta: 'Z', eta: 'H', teta: 'Θ', iota: 'I', kappa: 'K',
        lambda: 'Λ', mi: 'M', ni: 'N', csi: 'Ξ', omicron: 'O',
        phi: 'Π', ro: 'P', sigma: 'Σ', tau: 'T', upsilon: 'Y',
        fi: 'Φ', chi: 'X', psi: 'Ψ', omega: 'Ω'
    };

    return dictionary[word];
}

function findMaxValueInArray(array) {
    let max;
    let counter = 0;

    for (let index = 0; index < array.length; index++) {
        counter++;
        if (max == undefined || max < array[index]) {
            max = array[index];
        }
    }

    return max;
}

function findDuplicatedOnArray(array) {
    const duplicated = [];

    for (let outter = 0; outter < array.length; outter++) {
        for (let inner = 0; inner < array.length; inner++) {

            if (outter != inner && array[outter] == array[inner]) {
                duplicated.push(array[outter]);
            }
        }
    }

    return Array.from(new Set(duplicated));
}

function findXYZbyIterations(target) {
    let solutions = 0;

    for (let x = 0; x < target; x++) {
        for (let y = 0; y < target; y++) {
            for (let z = 0; z < target; z++) {
                if (3 * x + 9 * y + 8 * z === 79) {
                    solutions++;
                }
            }
        }
    }

    return solutions;
}

function indexOf(array, target, offset = 0) {
    let half = parseInt(array.length / 2);
    let current = array[half];

    if (current == target) {
        return offset + half;

    } else if (target > current) {
        let right = array.slice(half);
        return indexOf(right, target, offset + hald);
    } else {
        let left = array.slice(0, half);
        return indexOf(left, target, offset);
    }
}

// ---------------------------------------------------------------------
// Actions
// ---------------------------------------------------------------------
console.log('');
console.log('Big O constant: O(1)');
console.log('   - Check if a number is even or odd');
console.log('   --- Example, value 10: ' + isEvenOrOdd(10));
console.log('   --- Example, value 11: ' + isEvenOrOdd(11));
console.log('');
console.log('   - Find a value in map');
console.log('   --- Example, value csi: ' + findGreekSymbol('csi'));
console.log('   --- Example, value gamma: ' + findGreekSymbol('gamma'));
console.log('');
console.log('');
console.log('Big O logarithmic: O(log n)');
console.log('   - Find max value on array');
console.log('   -- Example, array [3, 1, 2]: ' + findMaxValueInArray([3, 1, 2]));
console.log('   -- Example, array [4, 5, 6, 1, 9, 2, 8, 3, 7]: ' + findMaxValueInArray([4, 5, 6, 1, 9, 2, 8, 3, 7]));
console.log('');
console.log('');
console.log('Big O quadratic: O(n^2)');
console.log('   - Find duplicated');
console.log('   -- Example, array [1, 2, 3, 4, 2, 2]: ' + findDuplicatedOnArray([1, 2, 3, 4, 2, 2]));
console.log('   -- Example, array [1, 2, 3, 4, 5, 6, 7, 8, 9, 3]: ' + findDuplicatedOnArray([1, 2, 3, 4, 5, 6, 7, 8, 9, 3]));
console.log('');
console.log('');
console.log('Big O polynomial: O(n^c)');
console.log('   - N loops');
console.log('   -- Example, find XYZ in "3*x + 9*y + 8*z === 79" with 10 iretations: ' + findXYZbyIterations(10));
console.log('   -- Example, find XYZ in "3*x + 9*y + 8*z === 79" with 20 iretations: ' + findXYZbyIterations(20));
console.log('');
console.log('');
console.log('Big O logarithmic time: O(log n)');
console.log('   - Binary search');
console.log('   -- Example, index of "[3, 1, 2]": ' + indexOf([3, 1, 2], 1));
console.log('   -- Example, index of "[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]": ' + indexOf([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 6));
