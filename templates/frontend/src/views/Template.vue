<template>
  <main-layout>
    <div class="heading">
      <h1>Certificate Templates</h1>
    </div>
    <div class="divider"></div>
    <div class="divider"></div>
    <div class="block">
      <div class="temp" id="09" v-on:click="select($event)">
        <img src="../assets/certificate09.jpg" class="certi_image" />
        <div class="certi_id">Template ID : 09</div>
      </div>
      <div class="temp" id="10" v-on:click="select($event)">
        <img src="../assets/certificate10.jpg" class="certi_image" />
        <div class="certi_id">Template ID : 10</div>
      </div>
      <div class="temp" id="03" v-on:click="select($event)">
        <img src="../assets/certificate03.jpg" class="certi_image" />
        <div class="certi_id">Template ID : 03</div>
      </div>
      <div class="temp" id="04" v-on:click="select($event)">
        <img src="../assets/certificate04.jpg" class="certi_image" />
        <div class="certi_id">Template ID : 04</div>
      </div>
    </div>
    <div class="block">
      <div class="temp" id="05" v-on:click="select($event)">
        <img src="../assets/certificate05.jpg" class="certi_image" />
        <div class="certi_id">Template ID : 05</div>
      </div>
      <div class="temp" id="06" v-on:click="select($event)">
        <img src="../assets/certificate06.jpg" class="certi_image" />
        <div class="certi_id">Template ID : 06</div>
      </div>
      <div class="temp" id="07" v-on:click="select($event)">
        <img src="../assets/certificate07.jpg" class="certi_image" />
        <div class="certi_id">Template ID : 07</div>
      </div>
      <div class="temp" id="08" v-on:click="select($event)">
        <img src="../assets/certificate08.jpg" class="certi_image" />
        <div class="certi_id">Template ID : 08</div>
      </div>
    </div>
    <div class="divider"></div>
    <div class="divider"></div>
    <div class="Feedback-modal">
      <modal
        name="modal-login"
        @opened="opened"
        :adaptive="true"
        :height="240"
        :width="340"
      >
        <div class="certy-modal">
          Are you sure you want to choose this template ??
          <div class="certy-temp">Template ID : {{ certiID }}</div>
          <div class="modal-button">
            <router-link
              :to="{ name: 'create', params: { certiID }}"
              class="certy-btn"
            >
              Create Certificate
            </router-link>
            <p class="back-btn">Choose another template</p>
          </div>
        </div>
      </modal>
    </div>
  </main-layout>
</template>

<script>
import MainLayout from "../components/layout/Main";

export default {
  components: {
    MainLayout,
  },
  data() {
    return {
      certiID: 0,
    };
  },
  methods: {
    select: function (event) {
      event.preventDefault();
      this.$modal.show("modal-login");
      this.certiID = event.currentTarget.id;
      //alert(event.currentTarget.id); // returns corresponding id
    },
    opened() {
      this.$refs.email.focus();
    },
    hide() {
      this.$modal.hide("modal-login");
    },
  },
};
</script>

<style scoped>
.block {
  display: flex;
  flex-direction: row;
  width: 100vw;
  padding-left: 20px;
}
.heading {
  margin: 15px;
  font-size: 22px;
  font-weight: bolder;
  color: #0d1413;
}
.temp {
  width: 330px;
  height: 260px;
}
.certi_image {
  cursor: pointer;
  height: 93%;
  border: 2px dashed #001716;
  padding: 3px;
}
.certi_image:hover {
  border: 2px solid #001716;
  background-color: #001716;
}
h1 {
  text-align: center;
}
.divider {
  border-bottom: 2px solid #001716;
  margin: 18px;
}
.certi_id {
  background-color: #001716;
  color: #fff;
  position: relative;
  bottom: 30px;
  margin-right: 20px;
}
.certy-btn {
  color: #4a8280;
  padding: 5px 15px;
  border: 1px solid #4a8280;
  background-color: #0d1413;
  border-radius: 32.33px;
  text-decoration: none;
  font-weight: bold;
}
.certy-btn:hover {
  color: #0d1413;
  border: 1px solid #0d1413;
  background-color: #4a8280;
}
.certy-modal {
  padding: 10px;
  margin: 10px;
  font-size: 18px;
  height: 220px;
  border: 1px solid #4a8280;
}
.certy-temp {
  padding-top: 20px;
  font-weight: bold;
}
.modal-button {
  position: absolute;
  top: 70%;
  bottom: 0;
  left: 23%;
}
.back-btn {
  cursor: pointer;
  padding-top: 10px;
  padding-left: 20px;
  font-size: 12px;
  color: #0d1413;
}
.back-btn:hover {
  color: #4a8280;
}
</style>
