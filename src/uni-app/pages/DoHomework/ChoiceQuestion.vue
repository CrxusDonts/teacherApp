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
        for (let i = 0; i < this.options.length; i++) {
            this.options[i].checked = false;
        }
    },
    methods: {
        CheckboxChange(e) {
            const items = this.options;
            const values = e.detail.value;
            let i = 0; const lenI = items.length;
            for (; i < lenI; ++i) {
                items[i].checked = false;
                let j = 0; const lenJ = values.length;
                for (; j < lenJ; ++j) {
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
