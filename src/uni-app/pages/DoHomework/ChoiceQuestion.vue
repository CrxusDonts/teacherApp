<template>
	<view class="cu-card case">
		<view class="cu-item shadow">
			<view class="cu-item">
				<view class="content flex-sub padding">
					<view class="text-lg margin-left">{{order + '.' + choiceQuestion.text_content}}</view>
					<checkbox-group class="block" @change="CheckboxChange">
						<view v-for="option in options" class="margin-top margin-left">
							<checkbox :class="option.checked?'checked':''"
							:checked="option.checked?true:false" :value="option.order">
							</checkbox>
							{{String.fromCharCode("A".charCodeAt(0) - 1 + option.order)}}.{{option.text_content}}
						</view>
					</checkbox-group>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
export default {
    props: ['choiceQuestion', 'order', 'index'],
    name: 'ChoiceQuestion',
    data() {
        return {
            options: [
                {
                    order: 1,
                    text_content: '是',
                    if_correct: true
                },
                {
                    order: 2,
                    text_content: '不是',
                    if_correct: false
                }
            ],
            student_answers: [
                {
                    order: 1
                }
            ]
        };
    },
    created() {
        for (var i = 0; i < this.options.length; i++) {
            this.options[i].checked = false;
        }
    },
    methods: {
        CheckboxChange(e) {
            var items = this.options;
            var values = e.detail.value;
            for (var i = 0, lenI = items.length; i < lenI; ++i) {
                items[i].checked = false;
                for (var j = 0, lenJ = values.length; j < lenJ; ++j) {
                    if (items[i].order === values[j]) {
                        items[i].checked = true;
                        break;
                    }
                }
            }
        }
    }
};
</script>

<style>
</style>
