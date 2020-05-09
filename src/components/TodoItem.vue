<template>
    <b-list-group-item>
        <b-form-checkbox
                :id="todo.id"
                v-model="status"
                name="checkbox-1"
                value="accepted"
                unchecked-value="not_accepted"
        >
            {{todo.msg}}
        </b-form-checkbox>
        <b-list-group>
            <b-list-group-item>Cras justo odio</b-list-group-item>

        </b-list-group>

    </b-list-group-item>
</template>

<script>
    export default {
        props: {
            todo: {
                type: Object,
                required: true
            }
        }
    }
</script>