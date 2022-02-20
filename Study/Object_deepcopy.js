// 객체 깊은 복사(재귀)
var copyObjectDeep = function (target) {
    var result = {};
    if (typeof target === 'object' && target != null) {
        for (var prop in target) {
            result[prop] = copyObjectDeep(target[prop]);
        };
    } else {
        result = target;
    }
    return result;
};

// 객체 깊은 복사(json 활용)
var copyObjectDeepJson = function (target) {
    return JSON.parse(JSON.stringify(target));
}
// 메서드나 숨겨진 프로퍼티(__proto__)는 복사가 되지 않음