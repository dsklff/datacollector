<template>
    <div class="sidenav">
        <a class="logo" href="#">Diploma</a>
        <a class="profile" href="#">Profile</a>
        <a class="publications" href="#">Publications</a>
        <a class="logout" href="#">Log out</a>
    </div>
</template>

<script>

</script>

<style>

    .logo {
        pointer-events: none;
        font-size: 40px;
        font-style: inherit;
    }

    .sidenav {
        height: 100%;
        width: 270px;
        position: fixed;
        z-index: 1;
        top: 0;
        left: 0;
        background-color: #111;
        overflow-x: hidden;
        padding-top: 20px;
        font-family: "Helvetica Neue", sans-serif;
    }

    .sidenav a {
        padding: 6px 8px 6px 16px;
        text-decoration: none;
        font-size: 25px;
        color: #818181;
        display: block;
    }

    .sidenav a:hover {
        color: #f1f1f1;
    }



    .main {
        margin-left: 160px; /* Same as the width of the sidenav */
        font-size: 28px; /* Increased text to enable scrolling */
        padding: 0px 10px;
    }

    @media screen and (max-height: 450px) {
        .sidenav {padding-top: 15px;}
        .sidenav a {font-size: 18px;}
    }
</style>
