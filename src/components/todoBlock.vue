<template class="mt-3">
    <div>
        <div class="row bg-light border p-3">
            <b-list-group>
                <TodoItem
                    v-for="todo of todos"
                    v-bind:todo="todo"
                />
            </b-list-group>
        </div>
    </div>
</template>

<script>
    import TodoItem from '@/components/TodoItem.vue'

    export default {
        props:['todos'],
        components: {
            TodoItem
        }
    }
</script>
